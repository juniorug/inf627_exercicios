#!/usr/bin/env python

import abc
import time
#from concretefactory.humiditySensorFactory import HumididtySensorFactory
from threading import Thread
import traceback

class HumidityReader(object):
    '''
    classdocs
    '''
    __metaclass__ = abc.ABCMeta

    def __init__(self, sensorName="DHT11Humididty"):
        '''
        Constructor
        '''
        #dht11 = HumididtySensorFactory.createSensor(sensorName)
        self.sensor = Sensor()
        self.threadSensor = Thread(target = self.measureHumidity, args=(self.sensor,5))
        self.threadSensor.daemon = True

    def startThread(self):
        print "inside startThread" 
        self.threadSensor.start()

    def pauseThread(self):
        print "inside pauseThread" 
        self.threadSensor.

    def releaseThread(self):
        print "inside releaseThread" 
        self.threadSensor.release()
        
    def measureHumidity(self,sensor, delay):
        try:
            while (True) :
                self.sensor.getHumidity()         #salvar aqui no banco a leitura
                time.sleep(delay)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            print "saindo da thread"


class Sensor(object):
    '''
    classdocs
    '''
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        '''
        Constructor
        '''
        print ("Sensor created")

    def getHumidity(self):
        """Setup the GPIO."""
        print ("Sensor reading. humidity: XX%")

    def __del__(self):
        """ We're no longer using the GPIO, so tell software we're done."""


hr = HumidityReader()
try:
    hr.startThread()
except:
    print "saindo do main"
    traceback.print_exc()

while (True):
    time.sleep(1)
    
