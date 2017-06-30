#!/usr/bin/python3
# -*- coding: utf-8 -*-

from private import *
import youtube_dl
import os, sys, subprocess

donloadDIR='/mnt/LOCAL/PrivStore/Videos/Clips/001-Downloads/'
downloadLIST1='/mnt/LOCAL/PrivStore/Videos/download.list'
ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

with open(downloadLIST1, 'r') as dl_list:
    lines=dl_list.readlines()
    for line in lines:
        with ydl:
            result = ydl.extract_info(line, download=True)
        if 'entries' in result:
            # Can be a playlist or a list of videos
            video = result['entries'][0]
        else:
            # Just a video
            video = result
        print(video)
