#!/bin/python3
import sys
from PyQt4 import QtGui

USA=['us-california.privateinternetaccess.com', 'us-east.privateinternetaccess.com', 'us-midwest.privateinternetaccess.com', 'us-chicago.privateinternetaccess.com', 'us-texas.privateinternetaccess.com', 'us-florida.privateinternetaccess.com', 'us-seattle.privateinternetaccess.com', 'us-west.privateinternetaccess.com', 'us-siliconvalley.privateinternetaccess.com', 'us-newyorkcity.privateinternetaccess.com']
CANADA=['ca-toronto.privateinternetaccess.com', 'ca.privateinternetaccess.com']
NETHERLANDS=['nl.privateinternetaccess.com']
SWEEDEN=['sweeden.privateinternetaccess.com']
NORWAY=['no.privateinternetaccess.com']
DENMARK=['denmark.privateinternetaccess.com']
SWITZERLAND=['swiss.privateinternetaccess.com']
FRANCE=['france.privateinternetaccess.com']
GERMANY=['germany.privateinternetaccess.com']
IRELAND=['ireland.privateinternetaccess.com']
ITALY=['italy.privateinternetaccess.com']

COUNTRIES=[USA, CANADA, NETHERLANDS, SWEEDEN, NORWAY, DENMARK, SWITZERLAND, FRANCE, GERMANY, IRELAND, ITALY]

ALLHOSTS=[]
for X in COUNTRIES:
	ALLHOSTS.extend(X)
