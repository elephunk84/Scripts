#!/bin/bash

cd /home/pi/GitRepo/centralheating/resources/python/
python ./read_temp.py &
python ./monitor.py &
