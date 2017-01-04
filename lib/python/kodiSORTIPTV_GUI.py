#!/bin/python3
import datetime, os, sys, collections, glob, re, subprocess, itertools
from shutil import move
from tempfile import NamedTemporaryFile

os.chdir("/home/iainstott/Kodi/IPTVLists")
channelDIR="Channels"
data=''

date=datetime.datetime.now().strftime("%d-%m-%y")
m3u1FILE=("Archive/"+str(date)+"_1.m3u")
m3u2FILE=("Archive/"+str(date)+"_2.m3u")
M3UFILES=[m3u1FILE, m3u2FILE]
m3uFILE="IPTV.m3u"
mym3uFILE="MYIPTV.m3u"
channellist="Channel_LIST.txt"
fileHEADER="#EXTM3U"
lineSTART="#EXTINF:-1,"

mychannelsDICT={}
channels={}

def buildDICTIONARIES ():
	with open(channellist, 'rU') as mychannels:
		for line in mychannels:
			name=line.rsplit('|',1)
			name=(name[1])
			channel=line.split("|", 1)[0]
			group=line.split("|",1)[1]
			group=group.split("|",1)[0]
			data=(channel, group)
			mychannelsDICT[name]=data
	with open(m3u1FILE, 'r') as availChannels:
		data = availChannels.read().splitlines(True)
	with open(m3u2FILE, 'w') as fout:
		fout.writelines(data[1:])
	with open(m3u2FILE) as f:
		for line1,line2 in itertools.izip_longest(*[f]*2):
			print(line1,line2)
			
if __name__ == "__main__":
	buildDICTIONARIES()
