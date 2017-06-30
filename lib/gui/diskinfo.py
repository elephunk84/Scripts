#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, math
from collections import namedtuple

_ntuple_diskusage = namedtuple('usage', 'total used free percent')

def percentage(part, whole):
  return 100 * float(part)/float(whole)

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])
   

def disk_usage(path):
    st = os.statvfs(path)
    free = convert_size(st.f_bavail * st.f_frsize)
    total = convert_size(st.f_blocks * st.f_frsize)
    used = convert_size((st.f_blocks - st.f_bfree) * st.f_frsize)
    totalOrig = st.f_blocks * st.f_frsize
    usedOrig = (st.f_blocks - st.f_bfree) * st.f_frsize
    percent = percentage(usedOrig, totalOrig)
    percent = str("%.2f" % percent) 
    return _ntuple_diskusage(total, used, free, percent)
    
if __name__ == "__main__":
    filesystem="/mnt/NFS/Backup"
    total, used, free = disk_usage(filesystem)
    print(filesystem+" = ("+total+" Total) ("+used+" Used) ("+free+" Free)")
