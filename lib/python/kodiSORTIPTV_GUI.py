#!/bin/python3
import datetime, os, sys, collections, glob, re, subprocess, itertools

os.chdir("/home/iainstott/Kodi/")
channelDIR="Channels"
data=''

date=datetime.datetime.now().strftime("%d-%m-%y")
m3u1FILE=("IPTVLists/Archive/"+str(date)+"_1.m3u")
m3u2FILE=("IPTVLists/Archive/"+str(date)+"_2.m3u")
M3UFILES=[m3u1FILE, m3u2FILE]
m3uFILE="IPTVLists/IPTV.m3u"
mym3uFILE="IPTVLists/MYIPTV.m3u"
channellist="IPTVLists/Channel_LIST.txt"
fileHEADER="#EXTM3U"
lineSTART="#EXTINF:-1,"
webgrabCONFIG="WebGrab/WebGrab++.config.xml"
webgrabSTART="WebGrab/config.start"
webgrabEND="WebGrab/config.end"


mychannelsDICT={}
mychannelsDICTMASTER={}
availchannelsDICT={}

def renumberCHANNELS ():
	number=1
	with open('IPTVLists/channelstemp.txt', 'w') as f:
		with open('IPTVLists/Channel_LIST.txt', 'r') as channelfile:
			lines=channelfile.readlines()
			for line in lines:
				line=line.split(" | ",1)[1]
				f.write(line)
	with open('IPTVLists/Channel_LIST.txt', 'w') as channellist:
		with open('IPTVLists/channelstemp.txt', 'r') as f:
			lines2=f.readlines()
			for line in lines2:
					number2="{:0>3}".format(number) 
					channellist.write(number2+' | '+line)
					number+=1
	os.remove('IPTVLists/channelstemp.txt')
					
def buildDICTIONARIES ():
	with open(channellist, 'rU') as mychannels:
		for line in mychannels:
			try:
				(channel, group, name, site, idnumber)=line.split(' | ')
				idnumber=idnumber.strip('\n')
				data=(channel, group, name, site, idnumber)
			except ValueError:
				(channel, group, name)=line.split(' | ')
				name=name.strip('\n')
				data=(channel, group, name)
			mychannelsDICT[name]=data
	with open(m3u1FILE, 'r') as availChannels:
		data = availChannels.read().splitlines(True)
	with open(m3u2FILE, 'w') as fout:
		fout.writelines(data[1:])
	with open(m3u2FILE, 'r') as f:
		with open('IPTVLists/Channels.txt', 'w') as channelsfile:
			for line in f:
				line=line.split(',',1)[1]
				nextline=next(f)
				m3ulink=nextline.rstrip('\n')
				try:
					line=line.replace(":", " | ")
					line=line.replace("| ", "  | ")
					line=line.replace(" l ", " | ")
					line=line.replace("DE ", "DE | ")
					line=line.replace("24-7 ", "24/7  | ")
					if "Five" not in line:
						line=line.replace("USA", "USA | ")
					else:
						line=line
					line2=(' '.join(line.split()))
					line2=line2.replace("USA | |", "USA |")
					line2=line2.replace("24/7 | |", "24/7 |")
					line2=line2.replace("DE | |", "DE |")
					line2=line2.replace("VIP USA", "VIP")
					if "|" not in line2:
						line3=("VOD | "+line2)
					else:
						line3=line2
					name=line3.rstrip('\n')
					chname=name.split('| ',1)[1]
					if chname in mychannelsDICT:
						line4=(line3+" | GOT")
					else:
						line4=line3
					if '*****' in line3:
						pass
					else:
						channelsfile.write(line4+'\n')
					availchannelsDICT[chname]=m3ulink
				except IndexError:
					pass
				continue
				channelsfile.close()
	with open('IPTVLists/Channels.txt', 'r') as channellistsorting:
		lines=channellistsorting.readlines()
		lines.sort()
	with open('IPTVLists/Channels.txt', 'w') as channellistsorted:
		for line in lines:
			channellistsorted.write(line)
	
def buildMasterDICT ():
	for key in mychannelsDICT.keys() & availchannelsDICT.keys():
		name=key
		name=name.replace('&', 'and')
		data=mychannelsDICT[key]
		channel=data[0]
		group=data[1]
		link=availchannelsDICT[key]
		try:
			site=data[3]
			idnumber=data[4]
			link=availchannelsDICT[key]
			data2=[name, group, link, site, idnumber]
		except (ValueError, IndexError) as e:
			data2=[name, group, link]
		mychannelsDICTMASTER[channel]=data2
	with open('IPTVLists/NotFound.txt', 'w') as notfound:
		for key in list(mychannelsDICT.keys()):
			if key not in availchannelsDICT:
				notfound.write(key+'\n')
	with open('IPTVLists/NotFound.txt', 'r') as notfoundsorting:
		lines=notfoundsorting.readlines()
		lines.sort()
	with open('IPTVLists/NotFound.txt', 'w') as notfoundsorted:
		for line in lines:
			notfoundsorted.write(line)

def buildM3UFILE ():
	with open(m3uFILE, 'w') as f:
		with open(mym3uFILE, 'w') as myf:
			f.write(fileHEADER+'\n')
			myf.write(fileHEADER+'\n')
			channels=collections.OrderedDict(sorted(mychannelsDICTMASTER.items()))
			for key, value in channels.items():
				name=(value[0])
				group=(value[1])
				link=(value[2])
				if name in ("ITV +1", "ITV 2 +1", "ITV 3 +1", "ITV 4 +1"):
					lineSTART="#EXTINF:-0,"
				else:
				    lineSTART="#EXTINF:-1,"
				link2=link.replace("IainStott", "IainStott2")
				if "Adult" not in group:
						f.write(lineSTART+str(group)+' | '+str(name)+'\n')
						f.write(str(link)+'\n')
						myf.write(lineSTART+str(group)+' | '+str(name)+'\n')
						myf.write(str(link2)+'\n')
				else:
					myf.write(lineSTART+str(group)+' | '+str(name)+'\n')
					myf.write(str(link2)+'\n')
	f.close()
	myf.close()

def buildGUIDE ():
		with open(webgrabCONFIG, 'w') as config:
			with open(webgrabSTART, 'r') as start:
				lines=start.readlines()
				for line in lines:
					config.write(line)
			channels=collections.OrderedDict(sorted(mychannelsDICTMASTER.items()))
			for key, value in channels.items():
				if len(value) == 5:
					site=(value[3])
					name=(value[1]+' | '+value[0])
					idnumber=(value[4])
					guideLINE='	<channel update="'+'i'+'" site="'+site+'" site_id="'+idnumber+'" xmltv_id="'+name+'">'+name+'</channel>'
					config.write(guideLINE+'\n')
			with open(webgrabEND, 'r') as end:
				lines=end.readlines()
				for line in lines:
					config.write(line)
			config.write("</settings>")
		config.close()
		
if __name__ == "__main__":
	buildDICTIONARIES()
	buildMasterDICT()
	buildM3UFILE()
	buildGUIDE()
