#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, subprocess, socket, uuid, base64

workingdir="/home/iainstott/GitRepo/Scripts"
lib_path = os.path.abspath(os.path.join(workingdir, 'lib'))
sys.path.append(lib_path)

from hosts import *
from private import *

NetworkManagerDIR='/etc/NetworkManager/system-connections/'
NetworkManagerDIRCONTS=os.popen('ls '+NetworkManagerDIR)
VPNConfFile=workingdir+'/lib/gui/data/VPN.conf'

def delHOSTS():
    for configFILE in NetworkManagerDIRCONTS:
        configFILE=configFILE.rstrip('\n')
        if configFILE in MyNetworks:
            pass
        else:
            os.remove(NetworkManagerDIR+configFILE)

def genHOSTS():
        for k, v in PIAHOSTS.items():
            VPNHost=k
            for address in v:
                VPNAddress=address
        print("Generating Config For "+VPNHost)
        for k,v in UserDETAILS.items():
            if k == "PPTUserDetails":
                PPTUsername=v[0]
                PPTPassword=v[1]
        with open(VPNConfFile, 'r') as origCONF:
            lines=origCONF.readlines()
            newCONFFILE=NetworkManagerDIR+VPNHost
            with open(newCONFFILE, 'w') as newCONF:
                for line in lines:
                    if line == "id=###id###\n":
                        VPNHost=VPNHost.replace("_", " ")
                        line=line.replace("###id###", VPNHost)
                    if line == "uuid=###uuid###\n":
                        UUID=uuid.uuid4()
                        line=line.replace("###uuid###", str(UUID))
                    if line == "gateway=###gateway###\n":
                        line=line.replace("###gateway###", VPNAddress)
                    if line == "user=###username###\n":
                        line=line.replace("###username###", STRdecode(PPTUsername))
                    if line == "password=###password###\n":
                        line=line.replace("###password###", STRdecode(PPTPassword))
                    newCONF.write(line)
            subprocess.call(['chmod', '0600', newCONFFILE])


if __name__ == "__main__":
    delHOSTS()
    genHOSTS()
