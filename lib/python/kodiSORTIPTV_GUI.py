#!/bin/python3
import datetime, os, sys, collections, glob, re, subprocess, itertools

os.chdir("/home/iainstott/Kodi/IPTVLists")
channelDIR="Channels"
data=''

date=datetime.datetime.now().strftime("%d-%m-%y")
m3u1FILE=("Archive/"+str(date)+"_1.m3u")
m3u2FILE=("Archive/"+str(date)+"_2.m3u")
M3UFILES=[m3u1FILE, m3u2FILE]
m3uFILE="IPTV.m3u"
mym3uFILE="MYIPTV.m3u"
newm3u="NEW.m3u"
channellist="Channel_LIST.txt"
fileHEADER="#EXTM3U"
lineSTART="#EXTINF:-1,"

mychannelsDICT={}
mychannelsDICTMASTER={}
availchannelsDICT={}

def buildDICTIONARIES ():
	with open(channellist, 'rU') as mychannels:
		for line in mychannels:
			name=line.rsplit('|',1)
			name=(name[1])
			name=name.rstrip('\n')
			name=name[1:]
			channel=line.split("|", 1)[0]
			group=line.split("|",1)[1]
			group=group.split("|",1)[0]
			data=(channel, group)
			mychannelsDICT[name]=data
	with open(m3u1FILE, 'r') as availChannels:
		data = availChannels.read().splitlines(True)
	with open(m3u2FILE, 'w') as fout:
		fout.writelines(data[1:])
	with open(m3u2FILE, 'r') as f:
		with open('Channels.txt', 'w') as channelsfile:
			for line in f:
				line=line.split(',',1)[1]
				nextline=next(f)
				m3ulink=nextline.rstrip('\n')
				try:
					line=line.replace(": ", " | ")
					line=line.replace("USA: ", "USA  | ")
					line=line.replace("| ", "  | ")
					line=line.replace(" l ", " | ")
					line=line.replace("24/7 ", "24/7  | ")
					line=line.replace("Adult ", "XXX  | Adult ")
					channelsfile.write(line)
					name=line.rstrip('\n')
					name=name.split('| ',1)[1]
					availchannelsDICT[name]=m3ulink
				except IndexError:
					pass
				continue
				channelsfile.close()
		
def buildMasterDICT ():
	for key in mychannelsDICT.keys() & availchannelsDICT.keys():
		name=key
		data=mychannelsDICT[key]
		channel=data[0]
		group=data[1]
		link=availchannelsDICT[key]
		data2=[name, group, link]
		mychannelsDICTMASTER[channel]=data2

def buildM3UFILE ():
	with open(newm3u, 'w') as f:
		f.write(fileHEADER+'\n')
		channels=collections.OrderedDict(sorted(mychannelsDICTMASTER.items()))
		for key, value in channels.items():
			name=(value[0])
			group=(value[1])
			link=(value[2])
			f.write(lineSTART+str(group)+' | '+str(name)+'\n')
			f.write(str(link)+'\n')
	f.close()
			

if __name__ == "__main__":
	buildDICTIONARIES()
	buildMasterDICT()
	buildM3UFILE()
