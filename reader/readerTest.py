#!/usr/bin/env python

from reader import SensorReader
import time

delay = 2
temp_sensor_id = 1
hum_sensor_id = 2
light_sensor_id = 3

ht = SensorReader.createReader('Temperature', 'DHT11Temperature', delay, temp_sensor_id)
hh = SensorReader.createReader('Humidity','DHT11Humidity', delay, hum_sensor_id)
hl = SensorReader.createReader('Luminosity','LDR', delay, light_sensor_id)

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

