#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, subprocess

IainsLaptop={'Iains-Laptop':('192.168.0.10', 'AA:AA:AA:AA:AA')}
ElorasLaptop={'Eloras-Laptop':('192.168.0.11', 'AA:AA:AA:AA:AA')}
AlienServer={'AlienServer':('192.168.0.2', 'F0:4D:A2:DB:E0:D9')}
GigaServer={'GigaServer':('192.168.0.202', 'AA:AA:AA:AA:AA')}
TheBeastServer={'BeastServer':('192.168.0.99', '00:24:81:E9:17:8E')}
BackupServer={'BackupServer':('192.168.0.204', 'AA:AA:AA:AA:AA')}

Raspi1={'Raspi1':('192.168.1.1', 'AA:AA:AA:AA:AA')}
Raspi2={'Raspi2':('192.168.1.2', 'AA:AA:AA:AA:AA')}
Raspi3={'Raspi3':('192.168.1.3', 'AA:AA:AA:AA:AA')}
Raspi4={'Raspi4':('192.168.1.4', 'AA:AA:AA:AA:AA')}
Raspi5={'Raspi5':('192.168.0.5', 'AA:AA:AA:AA:AA')}
Raspi6={'Raspi6':('192.168.0.130', 'AA:AA:AA:AA:AA')}

pFsense={'Secure':('192.168.0.98', 'AA:AA:AA:AA:AA')}

PHYSICALSERVERS=[AlienServer, GigaServer, TheBeastServer, BackupServer, Raspi1, Raspi2, Raspi3, Raspi4, Raspi5, Raspi6]
VIRTUALSERVERS=[pFsense]

MyNetworks=['Password Is On The Fridge', 'It Hurts When IP', 'Death Star Free WiFi', 'LAN Solo', 'Searching....', 'HomeVPN']

LOCALHOSTS=[]
localHOSTLIST={}

for host in PHYSICALSERVERS:
    LOCALHOSTS.append(host)
for host in VIRTUALSERVERS:
    LOCALHOSTS.append(host)
for host in LOCALHOSTS:
    for key, value in host.items():
        localHOSTLIST[key]=value

PIAHOSTS={
        "AU_Melbourne":["aus-melbourne.privateinternetaccess.com"],
        "AU_Sydney":["aus.privateinternetaccess.com"],
        "Brazil":["brazil.privateinternetaccess.com"],
        "CA_Montreal":["ca.privateinternetaccess.com"],
        "CA_Toronto":["ca-toronto.privateinternetaccess.com"],
        "Denmark":["denmark.privateinternetaccess.com"],
        "Finland":["fi.privateinternetaccess.com"],
        "France":["france.privateinternetaccess.com"],
        "Germany":["germany.privateinternetaccess.com"],
        "Hong_Kong":["hk.privateinternetaccess.com"],
        "India":["in.privateinternetaccess.com"],
        "Ireland":["ireland.privateinternetaccess.com"],
        "Israel":["israel.privateinternetaccess.com"],
        "Italy":["italy.privateinternetaccess.com"],
        "Japan":["japan.privateinternetaccess.com"],
        "Mexico":["mexico.privateinternetaccess.com"],
        "Netherlands":["nl.privateinternetaccess.com"],
        "New_Zealand":["nz.privateinternetaccess.com"],
        "Norway":["no.privateinternetaccess.com"],
        "Romania":["ro.privateinternetaccess.com"],
        "Singapore":["sg.privateinternetaccess.com"],
        "South Korea":["kr.privateinternetaccess.com"],
        "Sweden":["sweden.privateinternetaccess.com"],
        "Switzerland":["swiss.privateinternetaccess.com"],
        "Turkey":["turkey.privateinternetaccess.com"],
        "UK_London":["uk-london.privateinternetaccess.com"],
        "UK_Southampton":["uk-southampton.privateinternetaccess.com"],
        "US_California":["us-california.privateinternetaccess.com"],
        "US_Chicago":["us-chicago.privateinternetaccess.com"],
        "US_East":["us-east.privateinternetaccess.com"],
        "US_Florida":["us-florida.privateinternetaccess.com"],
        "US_Midwest":["us-midwest.privateinternetaccess.com"],
        "US_New York City":["us-newyorkcity.privateinternetaccess.com"],
        "US_Seattle":["us-seattle.privateinternetaccess.com"],
        "US_Silicon Valley":["us-siliconvalley.privateinternetaccess.com"],
        "US_Texas":["us-texas.privateinternetaccess.com"],
        "US_West":["us-west.privateinternetaccess.com"],
        }
PIAHOSTList=list(PIAHOSTS.keys())

COUNTRIES=[
        {"USA":["US California", "US East", "US Chicago", "US Texas", "US Florida", "US Seattle", "US West", "US Silicone Valley", "US New York City"]},
        {"Canada":["CA Toronto", "CA Montreal"]},
        {"Australia":["AU Melbourne", "AU Sydney"]},
        {"UK":["UK London", "UK Southampton"]},
        "Netherlands",
        "Hong Kong",
        "India",
        "Romania",
        "Singapore",
        "South Korea",
        "Israel",
        "Japan",
        "Mexico",
        "New Zealand",
        "Turkey",
        "Brazil",
        "Sweeden",
        "Norway",
        "Denmark",
        "Switzerland",
        "France",
        "Germany",
        "Ireland",
        "Italy"
        ]

REGIONS={"AmericaAustralia" : ["USA", "Canada", "Brazil", "Australia", "New Zealand"],
        "Europe" : ["UK", "Netherlands", "Sweeden", "Norway", "Denmark", "Switzerland", "France", "Germany", "Ireland", "Italy", "Romania", "Turkey"],
        "AsiaPacific" : ["South Korea", "Hong Kong", "Singapore", "Japan", "Israel", "India"]}

AmericaAustralia=[]
Europe=[]
AsiaPacific=[]
ALLVPNCountries=[]
ALLVPNHosts=[]
REGIONLIST=[]
REGIONLIST.append("All")

for country in COUNTRIES:
    try:
        for key, values in country.items():
            for city in values:
                ALLVPNHosts.append(city)
            for region, countries in REGIONS.items():
                if key in countries:
                    if region == "AmericaAustralia":
                        AmericaAustralia.append(key)
                    if region == "Europe":
                        Europe.append(key)
                    if region == "AsiaPacific":
                        AsiaPacific.append(key)
    except:
        ALLVPNHosts.append(country)
        for region, countries in REGIONS.items():
            if country in countries:
                if region == "AmericaAustralia":
                    AmericaAustralia.append(country)
                if region == "Europe":
                    Europe.append(country)
                if region == "AsiaPacific":
                    AsiaPacific.append(country)

for region, countries in REGIONS.items():
    if region == "AmericaAustralia":
        region="Americas & South Pacific"
    if region == "AsiaPacific":
        region = "Asia & Middle East"
    REGIONLIST.append(region)
    for country in countries:
        ALLVPNCountries.append(country)
