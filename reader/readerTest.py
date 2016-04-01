#!/usr/bin/env python

from reader import SensorReader
import time

ht = SensorReader.createReader('Temperature', 'DHT11Temperature', 2, 1)
hh = SensorReader.createReader('Humidity','DHT11Humidity', 2, 2)
hl = SensorReader.createReader('Luminosity','LDR', 2, 3) 
try:
    ht.startThread()
    hh.startThread()
    hl.startThread()
    for i in range (0,10): 
        time.sleep(6)

        ht.pauseThread()
        hh.pauseThread()
        hl.pauseThread()

        time.sleep(6)

        hr.releaseThread()
        hr.releaseThread()
        hr.releaseThread() 

except (KeyboardInterrupt, SystemExit):
    raise

except:
    print "saindo do main"
    traceback.print_exc()

while (True):
    time.sleep(1)

