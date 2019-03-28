#!/usr/bin/python

import urllib;

from datetime import date
from datetime import timedelta

import datetime, calendar

lastSat = datetime.date.today()
oneday = datetime.timedelta(days=1)

while lastSat.weekday() != calendar.SATURDAY:
    lastSat -= oneday

shiz = lastSat.strftime("%Y-%m-%d");
baseurl = "https://restreams.rtrfm.com.au/shows/undergroundsolution_"
filetype = ".mp3"
url = baseurl + shiz + filetype
print url
filepre = "/tmp/underground"
file = filepre + shiz + filetype
print file
urllib.urlretrieve (url, file);
print "done"
