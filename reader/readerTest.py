#!/usr/bin/env python

from reader import SensorReader

hr  = SensorReader.createReader('Temperature', 'DHT11Temperature')
try:
    hr.startThread()
except:
    print "saindo do main"
    traceback.print_exc()

while (True):
    time.sleep(1)