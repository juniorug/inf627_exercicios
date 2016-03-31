#!/usr/bin/env python

import abc
import time
import traceback
from concretefactory.humiditySensorFactory import HumididtySensorFactory
from db import DB
from sensorReader import SensorReader 
from threading import Thread

class HumidityReader(SensorReader):
    '''
    classdocs
    '''
    __metaclass__ = abc.ABCMeta

    def __init__(self, sensorName = "DHT11Humididty", delay = 5, sensor_id = None):
        '''
        Constructor
        '''
        SensorReader.__init__(self, None, delay, sensor_id)
        self.sensor = HumididtySensorFactory.createSensor(sensorName)
        self.sensor.changeSetup(4)
        # self.threadSensor = Thread(target = self.measureHumidity, args=(self.sensor, delay))
        self.threadSensor.daemon = True
        
    def measure(self):
        self.measureHumidity()

    def measureHumidity(self):
        try:
            while (True) :
                value = self.sensor.getHumidity()         #salvar aqui no banco a leitura
                # self.insertData(value)
                self.saveData(value) 
                print ("Humidity: " + value + "%")
                time.sleep(self.delay)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            print "saindo da thread"
            traceback.print_exc()

    def insertData(self, value):
        db = DB(None, None, "localhost", None, 'mydb', 'mydb.db')
        db.insertSensorData(2, 1, value)
        print("inserted")
        
        
hr = HumidityReader()
try:
    hr.startThread()
except:
    print "saindo do main"
    traceback.print_exc()

while (True):
    time.sleep(1)
    
