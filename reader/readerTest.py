#!/usr/bin/env python

from reader import SensorReader
import time

ht = SensorReader.createReader('Temperature', 'DHT11Temperature',5)
hh = SensorReader.createReader('Humidity','DHT11Humididty',5)
hl = SensorReader.createReader('Luminosity','LDR',5) 
try:
    ht.startThread()
    hh.startThread()
    hl.startThread()
except:
    print "saindo do main"
    traceback.print_exc()

while (True):
    time.sleep(1)
