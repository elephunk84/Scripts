#!/bin/python3
import datetime, os, sys, collections, glob, re, subprocess

os.chdir("/home/iainstott/Kodi/IPTVLists")
channelDIR="Channels"

date=datetime.datetime.now().strftime("%d-%m-%y")
m3u1FILE=("Archive/"+str(date)+"_1.m3u")
m3u2FILE=("Archive/"+str(date)+"_2.m3u")
M3UFILES=[m3u1FILE, m3u2FILE]
m3uFILE="IPTV.m3u"
mym3uFILE="MYIPTV.m3u"

fileHEADER="#EXTM3U"
lineSTART="#EXTINF:-1,"
data=''

channels={
"001":"BBC 1 HD",
"002":"BBC 2 HD",
"003":"ITV HD",
"004":"Channel 4 HD",
"005":"Channel 5 HD",
"006":"BBC Three",
"007":"BBC Four",
"008":"ITV +1",
"009":"ITV 2",
"010":"ITV 2 +1",
"011":"ITV 3",
"012":"ITV 3 +1",
"013":"ITV 4",
"014":"ITV 4 +1",
"015":"ITV Encore",
"016":"ITV Be",
"017":"E4 HD",
"018":"E4 +1",
"019":"Channel 4 +1",
"020":"Channel 5 +1",
"021":"Sky 1 HD",
"022":"Sky 2",
"023":"Sky Atlantic",
"024":"Sky Living",
"025":"5 Star",
"026":"5 USA",
"027":"Universal",
"028":"Dave HD",
"029":"Quest",
"030":"Syfy HD",
"031":"DMAX",
"032":"Fox",
"033":"Watch",
"034":"Bravo",
"035":"Discovery HD",
"036":"Discovery Turbo",
"037":"Discovery Shed",
"038":"Discovery Science",
"039":"Discovery Investigation",
"040":"Discovery Real Time",
"041":"Discovery Showcase",
"042":"National Geographic",
"043":"National Geographic Wild",
"044":"Eden",
"045":"Eden +1",
"046":"History Channel",
"047":"History Channel +1",
"048":"H2",
"049":"Crime (CI)",
"050":"Sky Cinema Premiere",
"051":"Sky Cinema Hits",
"052":"Sky Cinema Greats",
"053":"Sky Cinema Disney",
"054":"Sky Cinema Christmas",
"055":"Sky Cinema Action",
"056":"Sky Cinema Comedy",
"057":"Sky Cinema Thriller",
"058":"Sky Cinema Drama/Romance",
"059":"Sky Cinema Scifi/Horror",
"060":"Sky Cinema Select",
"061":"Film4",
"062":"TCM",
"063":"Movies 24",
"064":"Movies4Men",
"065":"True Movies 1",
"066":"True Movies 2",
"067":"Disney Channel",
"068":"Disney XD",
"069":"Disney Jnr",
"070":"Nickelodeon",
"071":"Nicktoons",
"072":"Nick Jnr",
"073":"Cartoonito",
"074":"Cartoon Network",
"075":"Boomerang",
"076":"CBeebies",
"076":"CBBC Channel",
"077":"Sky Sports 1",
"078":"Sky Sports 2",
"079":"Sky Sports 3",
"080":"Sky Sports 4",
"081":"Sky Sports 5",
"082":"Sky Sports F1",
"083":"Sky Sports News",
"084":"Sky Sports Mix",
"085":"Sky Box Office 1",
"086":"Sky Box Office 2",
"087":"BT Sport 1",
"088":"BT Sport 2",
"089":"BT Sport 3",
"090":"BT Sport Extra 1",
"091":"BT Sport Extra 2",
"092":"BT Sport Extra 3",
"093":"BT Sport Extra 4",
"094":"BT Sport Extra 5",
"095":"Eurosport 1",
"096":"Eurosport 2",
"096":"Bein 1",
"097":"Bein 2",
"098":"Bein 3",
"099":"Bein 4",
"100":"Bein 5",
"101":"Bein 6",
"102":"Bein 7",
"103":"Bein 8",
"104":"Bein 9",
"105":"Bein 10",
"106":"Bein 11",
"107":"Bein 12",
"108":"Box Nation",
"109":"LFCTV"
}

def findMatchingFile (fileList, stringToMatch):
	global data
	data=''
	stringToMatch=re.sub(r'[\W_]', '',stringToMatch)
	stringToMatch=stringToMatch.lower()	
	for file in fileList:
		file2=file.split('_',1)[1]
		file3=re.sub('_', '', file2)
		file3=file3.lower()
		if (stringToMatch == "itv11"):
			data=(lineSTART+"ITV 1 +1"+'\n'+"http://live.zoptv.com/filmon/master.m3u8?id=1817"+'\n')
			pass
		if (stringToMatch == "itv21"):
			data=(lineSTART+"ITV 2 +1"+'\n'+"http://live.zoptv.com/filmon/master.m3u8?id=1820"+'\n')
			pass
		if (stringToMatch == "itv31"):
			data=(lineSTART+"ITV 3 +1"+'\n'+"http://live.zoptv.com/filmon/master.m3u8?id=1823"+'\n')
			pass
		if (stringToMatch == "itv41"):
			data=(lineSTART+"ITV 4 +1"+'\n'+"http://live.zoptv.com/filmon/master.m3u8?id=1826"+'\n')
			pass
		if file3.startswith(stringToMatch):
			if (stringToMatch) in file3:
				filename=(channelDIR+"/"+file)
				with open(filename, "rb") as f:
					first = f.readline()      # Read the first line.
					f.seek(-2, 2)             # Jump to the second last byte.
					while f.read(1) != b"\n": # Until EOL is found...
						f.seek(-2, 1)         # ...jump back the read byte plus one more.
					last = f.readline()       # Read last line.
				m3ulink=str(last)
				m3ulink=m3ulink[2:]
				m3ulink=m3ulink[:-5]
				m3ulink=m3ulink+'\n'
				data=(lineSTART+v+'\n'+m3ulink+'\n')
				pass
	if not data:
		data=(lineSTART+v+'\n'+"http:// "+'\n')
	return data
	
if __name__ == "__main__":
	lastch=''
	channels=collections.OrderedDict(sorted(channels.items()))
	global channel
	global v
	channelList=os.listdir(channelDIR)
	with open(m3uFILE, 'w') as f:
		f.write(fileHEADER+'\n')
		for k, v in channels.items():
			channel=re.sub(r'[\W_]', '_', v)
			if channel is not lastch:
				findMatchingFile(channelList, channel)
				f.write(data)
				lastch=channel
		f.close()
	with open(m3uFILE,'r+') as file:
		with open(mym3uFILE, 'w') as out:
			for line in file:
				if not line.isspace():
					out.write(line)
		out.close()
	file.close()
	with open(mym3uFILE,'r+') as file:
		with open(m3uFILE, 'w') as out:
			for line in file:
				if not line.isspace():
					out.write(line)
		out.close()
	file.close()
	f = open(mym3uFILE,'r')
	filedata = f.read()
	f.close()
	newdata = filedata.replace("IainStott","IainStott2")
	f = open(mym3uFILE,'w')
	f.write(newdata)
	f.close()
