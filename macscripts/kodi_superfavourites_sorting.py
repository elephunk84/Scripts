#!/bin/python3
import subprocess
import os
os.chdir("/Users/iainstott/OneDrive/Dev/Scripts/macscripts/")


subprocess.call(['./kodi_superfavourites_creation'])        
subprocess.call(['./kodi_superfavourites_xmlcreation'])       
with open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/skysports1.txt", "r") as ins:
    for line in ins:
        Name, URL = line.split("=", 1)
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/name.txt", "w")
        f.write( repr(Name) )
        f.close()
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/url.txt", "w")
        f.write( repr(URL) )
        f.close()
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/channel.txt", "w")
        f.write( "Sky Sports 1" )
        f.close()
        subprocess.call(['./kodi_superfavourites_xmlinsertion'])
subprocess.call(['./kodi_superfavourites_xmlclose'])        

subprocess.call(['./kodi_superfavourites_xmlcreation'])       
with open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/skysports2.txt", "r") as ins:
    for line in ins:
        Name, URL = line.split("=", 1)
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/name.txt", "w")
        f.write( repr(Name) )
        f.close()
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/url.txt", "w")
        f.write( repr(URL) )
        f.close()
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/channel.txt", "w")
        f.write( "Sky Sports 2" )
        f.close()
        subprocess.call(['./kodi_superfavourites_xmlinsertion'])
subprocess.call(['./kodi_superfavourites_xmlclose'])        

subprocess.call(['./kodi_superfavourites_xmlcreation'])       
with open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/skysports3.txt", "r") as ins:
    for line in ins:
        Name, URL = line.split("=", 1)
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/name.txt", "w")
        f.write( repr(Name) )
        f.close()
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/url.txt", "w")
        f.write( repr(URL) )
        f.close()
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/channel.txt", "w")
        f.write( "Sky Sports 3" )
        f.close()
        subprocess.call(['./kodi_superfavourites_xmlinsertion'])
subprocess.call(['./kodi_superfavourites_xmlclose'])        

subprocess.call(['./kodi_superfavourites_xmlcreation'])       
with open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/skysports4.txt", "r") as ins:
    for line in ins:
        Name, URL = line.split("=", 1)
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/name.txt", "w")
        f.write( repr(Name) )
        f.close()
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/url.txt", "w")
        f.write( repr(URL) )
        f.close()
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/channel.txt", "w")
        f.write( "Sky Sports 4" )
        f.close()
        subprocess.call(['./kodi_superfavourites_xmlinsertion'])
subprocess.call(['./kodi_superfavourites_xmlclose'])        

subprocess.call(['./kodi_superfavourites_xmlcreation'])       
with open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/skysports5.txt", "r") as ins:
    for line in ins:
        Name, URL = line.split("=", 1)
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/name.txt", "w")
        f.write( repr(Name) )
        f.close()
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/url.txt", "w")
        f.write( repr(URL) )
        f.close()
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/channel.txt", "w")
        f.write( "Sky Sports 5" )
        f.close()
        subprocess.call(['./kodi_superfavourites_xmlinsertion'])
subprocess.call(['./kodi_superfavourites_xmlclose'])        

subprocess.call(['./kodi_superfavourites_xmlcreation'])       
with open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/skysportsF1.txt", "r") as ins:
    for line in ins:
        Name, URL = line.split("=", 1)
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/name.txt", "w")
        f.write( repr(Name) )
        f.close()
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/url.txt", "w")
        f.write( repr(URL) )
        f.close()
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/channel.txt", "w")
        f.write( "Sky Sports F1" )
        f.close()
        subprocess.call(['./kodi_superfavourites_xmlinsertion'])
subprocess.call(['./kodi_superfavourites_xmlclose'])        

subprocess.call(['./kodi_superfavourites_xmlcreation'])       
with open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/lfc.txt", "r") as ins:
    for line in ins:
        Name, URL = line.split("=", 1)
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/name.txt", "w")
        f.write( repr(Name) )
        f.close()
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/url.txt", "w")
        f.write( repr(URL) )
        f.close()
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/channel.txt", "w")
        f.write( "Liverpool FC TV" )
        f.close()
        subprocess.call(['./kodi_superfavourites_xmlinsertion'])
subprocess.call(['./kodi_superfavourites_xmlclose']) 

subprocess.call(['./kodi_superfavourites_xmlcreation'])       
with open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/bein.txt", "r") as ins:
    for line in ins:
        Name, URL = line.split("=", 1)
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/name.txt", "w")
        f.write( repr(Name) )
        f.close()
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/url.txt", "w")
        f.write( repr(URL) )
        f.close()
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/channel.txt", "w")
        f.write( "Bein Sports" )
        f.close()
        subprocess.call(['./kodi_superfavourites_xmlinsertion'])
subprocess.call(['./kodi_superfavourites_xmlclose'])        

subprocess.call(['./kodi_superfavourites_xmlcreation'])       
with open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/skysportsnews.txt", "r") as ins:
    for line in ins:
        Name, URL = line.split("=", 1)
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/name.txt", "w")
        f.write( repr(Name) )
        f.close()
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/url.txt", "w")
        f.write( repr(URL) )
        f.close()
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/channel.txt", "w")
        f.write( "Sky Sports News" )
        f.close()
        subprocess.call(['./kodi_superfavourites_xmlinsertion'])
subprocess.call(['./kodi_superfavourites_xmlclose'])    

subprocess.call(['./kodi_superfavourites_xmlcreation'])       
with open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/eurosport1.txt", "r") as ins:
    for line in ins:
        Name, URL = line.split("=", 1)
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/name.txt", "w")
        f.write( repr(Name) )
        f.close()
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/url.txt", "w")
        f.write( repr(URL) )
        f.close()
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/channel.txt", "w")
        f.write( "Eurosports 1" )
        f.close()
        subprocess.call(['./kodi_superfavourites_xmlinsertion'])
subprocess.call(['./kodi_superfavourites_xmlclose'])    

subprocess.call(['./kodi_superfavourites_xmlcreation'])       
with open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/eurosport2.txt", "r") as ins:
    for line in ins:
        Name, URL = line.split("=", 1)
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/name.txt", "w")
        f.write( repr(Name) )
        f.close()
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/url.txt", "w")
        f.write( repr(URL) )
        f.close()
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/channel.txt", "w")
        f.write( "Eurosports 2" )
        f.close()
        subprocess.call(['./kodi_superfavourites_xmlinsertion'])
subprocess.call(['./kodi_superfavourites_xmlclose'])    

subprocess.call(['./kodi_superfavourites_xmlcreation'])       
with open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/btsports.txt", "r") as ins:
    for line in ins:
        Name, URL = line.split("=", 1)
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/name.txt", "w")
        f.write( repr(Name) )
        f.close()
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/url.txt", "w")
        f.write( repr(URL) )
        f.close()
        f = open("/Users/iainstott/Library/Application Support/Kodi/userdata/addon_data/script.renegadestv/channel.txt", "w")
        f.write( "BT Sports 1" )
        f.close()
        subprocess.call(['./kodi_superfavourites_xmlinsertion'])
subprocess.call(['./kodi_superfavourites_xmlclose'])    