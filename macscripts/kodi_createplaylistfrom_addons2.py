#!/bin/python3
import subprocess
import os
os.chdir("/Users/iainstott/OneDrive/Dev/Scripts/macscripts/")

import fileinput


subprocess.call(['./kodi_createplaylistfrom_addons2'])
inputFile = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/links.txt", 'r')
lineList = inputFile.readlines()
lineList.sort()
for line in lineList:
	f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/links2.txt", "a")
	f.write( line )
	f.close()
with open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/links2.txt", "r") as ins:
    for line in ins:
        Name, URL = line.split("=", 1)
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/name.txt", "w")
        f.write( repr(Name) )
        f.close()
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/url.txt", "w")
        f.write( repr(URL) )
        f.close()
        subprocess.call(['./kodi_createplaylistfrom_m3uinsertion'])
