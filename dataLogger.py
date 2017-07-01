#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, os.path, sys, subprocess, socket, sqlite3, threading, re
import math, glob
import datetime, time

hostname=socket.gethostname()
if hostname in IainsLaptop:
    workingdir="/mnt/NFS/Backup/GitRepo/Scripts"
if hostname == "alienhost":
    workingdir="/mnt/LOCAL/Backup/BackupFolder/Backup/GitRepo/Scripts"
if hostname in TheBeastServer:
    workingdir="/mnt/NFS/Backup/GitRepo/Scripts"

if hostname in IainsLaptop:
    heatingFOLDER="/mnt/NFS/Backup/GitRepo/Heating"
if hostname == "alienhost":
    heatingFOLDER="/mnt/LOCAL/Backup/BackupFolder/Backup/GitRepo/Heating"
if hostname in TheBeastServer:
    heatingFOLDER="/mnt/NFS/Backup/GitRepo/Heating"

lib_path = os.path.abspath(os.path.join(workingdir, 'lib'))
sys.path.append(lib_path)

from lib.gui.hosts import *
from lib.gui.diskinfo import *

guiFOLDER=workingdir+"/lib/gui"
guidataFOLDER=guiFOLDER+"/data"
bashFOLDER=workingdir+"/lib/bash"
pythonFOLDER=workingdir+"/lib/python"

dataTables=['systems', 'heating', 'storage']

RPI1=""
RPI2=""
RPI3=""
RPI4=""
RPI5=""
RPI6=""
AlienSrv=""
GigaSrv=""
BeastSrv=""
BackupSrv=""

CurrentTemp=''
SetTemp=''
CH_Status=''
ManOverride=''
AdvOverride=''
SummerMode=''
ManSummerMode=''

timer=0

def dateTime():
    dateTimeLIST=[]
    now=datetime.datetime.now()
    yesterday=datetime.datetime.now() - datetime.timedelta(days=1)
    yesterday=yesterday.strftime("%A %d/%B/%Y %H:%M")
    dateTimeLIST.append(now.strftime("%A"))
    dateTimeLIST.append(now.strftime("%d/%B/%Y"))
    dateTimeLIST.append(str(now.strftime("%H:%M:%S")))
    dateTimeLIST.append(str(now.strftime("%H:%M")))
    dateTimeLIST.append(yesterday)
    dateTimeLIST.append(now.strftime("%d"))
    dateTimeLIST.append(now.strftime("%B"))
    dateTimeLIST.append(now.strftime("%Y"))
    return dateTimeLIST

def MachineStatus():
    global RPI1, RPI2, RPI3, RPI4, RPI5, RPI6, AlienSrv, GigaSrv, BeastSrv, BackupSrv
    for dic in LOCALHOSTS:
        for key in dic.keys():
            HostName=key
            for val in dic.values():
                IP_Address=val[0]
            response = os.system("ping -c 1 " + IP_Address+" 2>&1 >/dev/null")
            if response == 0:
                pingstatus = "Online"
            else:
                pingstatus = "OFFLINE"
            if HostName in Raspi1:
                RPI1=pingstatus
            if HostName in Raspi2:
                RPI2=pingstatus
            if HostName in Raspi3:
                RPI3=pingstatus
            if HostName in Raspi4:
                RPI4=pingstatus
            if HostName in Raspi5:
                RPI5=pingstatus
            if HostName in Raspi6:
                RPI6=pingstatus
            if HostName in AlienServer:
                AlienSrv=pingstatus
            if HostName in GigaServer:
                GigaSrv=pingstatus
            if HostName in TheBeastServer:
                BeastSrv=pingstatus
            if HostName in BackupServer:
                BackupSrv=pingstatus
            else:
                pass
    return RPI1, RPI2, RPI3, RPI4, RPI5, RPI6, AlienSrv, GigaSrv, BeastSrv, BackupSrv

def getData():
    dateTimeLIST = dateTime()
    global RPI1, RPI2, RPI3, RPI4, RPI5, RPI6, AlienSrv, GigaSrv, BeastSrv, BackupSrv
    global CurrentTemp, SetTemp, CH_Status, ManOverride, AdvOverride, SummerMode, ManSummerMode
    RPI1, RPI2, RPI3, RPI4, RPI5, RPI6, AlienSrv, GigaSrv, BeastSrv, BackupSrv = MachineStatus()
    db=(heatingFOLDER+"/app/database/templogs/"+dateTimeLIST[7]+"/"+dateTimeLIST[6]+"/"+dateTimeLIST[5]+".db")
    with sqlite3.connect(db) as tempconn:
        curs=tempconn.cursor()
        curs.execute('SELECT * FROM temps ORDER BY ROWID DESC LIMIT 1')
        dbData=curs.fetchone()
        curs.execute('SELECT * FROM override ORDER BY ROWID DESC LIMIT 1')
        dbData2=curs.fetchone()
    CH_Status=dbData[6]
    CurrentTemp=str(dbData[1])
    SetTemp=str(dbData[7])
    ManOverride=dbData[4]
    AdvOverride=str(dbData[5])
    SummerMode=dbData2[4]
    ManSummerMode=dbData2[5]

def writeDB():
    global RPI1, RPI2, RPI3, RPI4, RPI5, RPI6, AlienSrv, GigaSrv, BeastSrv, BackupSrv
    global CurrentTemp, SetTemp, CH_Status, ManOverride, AdvOverride, SummerMode, ManSummerMode
    dateTimeLIST=dateTime()
    todaysDB=(guidataFOLDER+"/logger/"+dateTimeLIST[7]+"/"+dateTimeLIST[6]+"/"+dateTimeLIST[5]+"_datalogger.db")
    DBdir=os.path.dirname(todaysDB)
    getData()
    if os.path.isfile(todaysDB) and os.access(todaysDB, os.R_OK):
        pass
    else:
        print("Creating "+todaysDB)
        try:
            os.stat(guidataFOLDER)
        except:
            os.mkdir(guidataFOLDER)
        try:
            os.stat(guidataFOLDER+"/"+dateTimeLIST[7])
        except:
            os.mkdir(guidataFOLDER+"/"+dateTimeLIST[7])
        try:
            os.stat(guidataFOLDER+"/"+dateTimeLIST[7]+"/"+dateTimeLIST[6])
        except:
            os.mkdir(guidataFOLDER+"/"+dateTimeLIST[7]+"/"+dateTimeLIST[6])
        subprocess.call(['touch', todaysDB])
    with sqlite3.connect(todaysDB) as tempconn:
        curs=tempconn.cursor()
        tempTableCheck='create table if not exists ' + dataTables[0] + '(RPI1 text, RPI2 text, RPI3 text, RPI4 text, RPI5 text, RPI6 text, AlienServer text, GigaServer text, BeastServer text, BackupServer text);'
        curs.execute(tempTableCheck)
        curs.execute("INSERT INTO " + dataTables[0] + " values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",  (RPI1, RPI2, RPI3, RPI4, RPI5, RPI6, AlienSrv, GigaSrv, BeastSrv, BackupSrv) )
        overrideTableCheck='create table if not exists ' + dataTables[1] + '(CurrentTemp numeric, SetTemp numeric, Status text, manOverride text, AdvOverride text, SummerMode text, ManSummerMode);'
        curs.execute(overrideTableCheck)
        curs.execute("INSERT INTO " + dataTables[1] + " values (?, ?, ?, ?, ?, ?, ?);", (CurrentTemp, SetTemp, CH_Status, ManOverride, AdvOverride, SummerMode, ManSummerMode))
        #tempTableCheck='create table if not exists ' + dataTables[2] + '(day DATETIME, date DATETIME, timeBIG DATETIME, timeSMALL DATETIME, yesterday DATETIME);'
        #curs.execute(tempTableCheck)
        #curs.execute("INSERT INTO " + dataTables[2] + " values (?, ?, ?, ?, ?);", (dateTimeLIST[0], dateTimeLIST[1], dateTimeLIST[2], dateTimeLIST[3], dateTimeLIST[4]))
        tempconn.commit()

if __name__ == "__main__":
    while True:
        if timer == 10:
            writeDB()
            timer=0
            print("Record data...")
        timer += 1
        print(timer)
