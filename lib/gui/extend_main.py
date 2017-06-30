#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading, multiprocessing, os, platform, psutil, datetime, time, socket, subprocess, sqlite3, sys, matplotlib, math, base64
from requests import get
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")

from lib.gui.private import *
from lib.gui.diskinfo import *
from lib.gui.heatinginput import *
from lib.gui.settings import *
from lib.gui.koditools import *
from lib.gui.stringencode import *
from lib.gui.isotools import *

def get_diskInfo(filesystem):
    total, used, free, percent = disk_usage(filesystem)
    return str(filesystem+" = ("+total+" Total) ("+used+" Used) ("+free+" Free) "+percent+"% Used")

def clickAbout():
    clickabout_toplevel = Toplevel()
    clickabout_toplevel.geometry('200x100+300+300')
    label0 = Label(clickabout_toplevel, text="         ", height=0, width=100)
    label0.pack()
    label1 = Label(clickabout_toplevel, text="Ballsack", height=0, width=100)
    label1.pack()
    label2 = Label(clickabout_toplevel, text="Is Hairy", height=0, width=100)
    label2.pack()

def heatingGraphPage():
    heatingdb="/mnt/NFS/Backup/GitRepo/Heating/app/database/templogs/"+dateTimeLIST[7]+"/"+dateTimeLIST[6]+"/"+dateTimeLIST[5]+".db"
    with sqlite3.connect(heatingdb) as tempconn:
        curs=tempconn.cursor()
        curs.execute('SELECT temp, timestamp FROM temps ORDER BY ROWID ASC LIMIT 10000')
        graphData=curs.fetchall()
        graphData=graphData[::250]
        graphDataTEMP=[x[0] for x in graphData]
        graphDataTIME=[x[1] for x in graphData]
    heatingGraph_toplevel=Toplevel()
    g_label = Label(heatingGraph_toplevel, text="Graph Page!")
    g_label.pack(pady=10,padx=10)
    f_graph = Figure(figsize=(5,5), dpi=100)
    a_graph = f_graph.add_subplot(111)
    a_graph.plot(graphDataTEMP,graphDataTIME)
    canvas = FigureCanvasTkAgg(f_graph, heatingGraph_toplevel)
    canvas.show()
    canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
    toolbar = NavigationToolbar2TkAgg(canvas, heatingGraph_toplevel)
    toolbar.update()
    canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

def seconds_elapsed():
    try:
        f = open( "/proc/uptime" )
        contents = f.read().split()
        f.close()
    except:
        return "Cannot open uptime file: /proc/uptime"
    total_seconds = float(contents[0])
    MINUTE  = 60
    HOUR    = MINUTE * 60
    DAY     = HOUR * 24
    days    = int( total_seconds / DAY )
    hours   = int( ( total_seconds % DAY ) / HOUR )
    minutes = int( ( total_seconds % HOUR ) / MINUTE )
    seconds = int( total_seconds % MINUTE )
    string = ""
    if days > 0:
        string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
    if len(string) > 0 or hours > 0:
        string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
    if len(string) > 0 or minutes > 0:
        string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
    string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
    UPTIME=string
    return UPTIME

def get_info():
    HOSTNAME=socket.gethostname()
    OS=(platform.system())
    OS_VER=(platform.release())
    OS_Details=OS+" "+OS_VER
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    INTIP=s.getsockname()[0]
    s.close()
    EXTIP = get('https://api.ipify.org').text
    return HOSTNAME, OS, OS_VER, OS_Details, INTIP, EXTIP

