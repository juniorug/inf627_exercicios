#!/usr/bin/env python

from reader import TemperatureReader
import time


tr = TemperatureReader()
try:
    tr.startThread()
except:
    print "saindo do main"
    traceback.print_exc()

while (True):
    time.sleep(1)
