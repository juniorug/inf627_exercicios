#!/usr/bin/env python

import abc
import time
import traceback
from concretefactory.humiditySensorFactory import HumididtySensorFactory
from threading import Thread

class HumidityReader(object):
    '''
    classdocs
    '''
    __metaclass__ = abc.ABCMeta

    def __init__(self, sensorName="DHT11Humididty"):
        '''
        Constructor
        '''
        self.sensor = HumididtySensorFactory.createSensor(sensorName)
        self.sensor.changeSetup(4)
        self.threadSensor = Thread(target = self.measureHumidity, args=(self.sensor,5))
        self.threadSensor.daemon = True

    def startThread(self):
        print "inside startThread" 
        self.threadSensor.start()

    def pauseThread(self):
        print "inside pauseThread" 
        #self.threadSensor.

    def releaseThread(self):
        print "inside releaseThread" 
        self.threadSensor.release()
        
    def measureHumidity(self,sensor, delay):
        try:
            while (True) :
                #self.sensor.getHumidity()         #salvar aqui no banco a leitura
                print ("Humidity: " + sensor.getHumidity() + "%")
                time.sleep(delay)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            print "saindo da thread"


hr = HumidityReader()
try:
    hr.startThread()
except:
    print "saindo do main"
    traceback.print_exc()

while (True):
    time.sleep(1)
    
