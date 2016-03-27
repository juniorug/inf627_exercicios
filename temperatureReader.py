#!/usr/bin/env python

import abc
import time
import traceback
from concretefactory.temperatureSensorFactory import TemperatureSensorFactory
from threading import Thread

class TemperatureReader(object):
    '''
    classdocs
    '''
    __metaclass__ = abc.ABCMeta

    def __init__(self, sensorName="DHT11Temperature"):
        '''
        Constructor
        '''
        print "building sensor"
        self.sensor = TemperatureSensorFactory.createSensor(sensorName)
        self.sensor.changeSetup(4)
        self.threadSensor = Thread(target = self.measureTemperature, args=(self.sensor,5))
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
        
    def measureTemperature(self,sensor, delay):
        try:
            while (True) :
                self.sensor.getTemperature()         #salvar aqui no banco a leitura
                print ("Temperature: " + self.sensor.getTemperature() + u"\u00b0" + "C")
                time.sleep(delay)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            traceback.print_exc() 
            print "saindo da thread"


hr = TemperatureReader()
try:
    hr.startThread()
except:
    print "saindo do main"
    traceback.print_exc()

while (True):
    time.sleep(1)
    
