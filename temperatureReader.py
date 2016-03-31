#!/usr/bin/env python

import abc
import time
import traceback
from concretefactory.temperatureSensorFactory import TemperatureSensorFactory
from sensorReader import SensorReader 
from threading import Thread

class TemperatureReader(SensorReader):
    '''
    classdocs
    '''
    __metaclass__ = abc.ABCMeta

    def __init__(self, sensorName = "DHT11Temperature", delay = 5, sensor_id = None):
        '''
        Constructor
        '''
        SensorReader.__init__(self, None, delay, sensor_id)
        print "building sensor"
        self.sensor = TemperatureSensorFactory.createSensor(sensorName)
        self.sensor.changeSetup(4)
        # self.threadSensor = Thread(target = self.measureTemperature, args=(self.sensor,delay))
        self.threadSensor.daemon = True

    def measure(self):
        self.measureTemperature()
        
    def measureTemperature(self):
        try:
            while (True) :
                #self.sensor.getTemperature()         #salvar aqui no banco a leitura
                value = self.sensor.getTemperature()
                self.saveData(value) 
                print ("Temperature: " + value + u"\u00b0" + "C")
                time.sleep(self.delay)
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
    
