#!/usr/bin/env python

import abc
import time
import traceback
import RPi.GPIO as GPIO, os
from concretefactory.humiditySensorFactory import HumididtySensorFactory
from concretefactory.temperatureSensorFactory import TemperatureSensorFactory
from humidityReader import HumidityReader
from LightReader import LightReader
from temperatureReader import TemperatureReader
from threading import Thread
from models import SensorMesurement


class SensorReader(object):
    '''
    classdocs
    '''
    __metaclass__ = abc.ABCMeta

    def __init__(self, sensor = None, delay = 5, sensor_id = None):
        '''
        Constructor
        '''
        self.threadSensor = Thread(target = self.measure, args=())
        self.sensor = sensor
        self.delay = delay
        self.sensor_id = sensor_id

    @staticmethod
    def createReader(readerType, sensorType, delay):

        if (readerType == 'Temperature'):
            return TemperatureReader(sensorType, delay)
        elif(readerType == 'Humidity'):
            return HumidityReader(sensorType, delay)
        elif(readerType == 'Luminosity'):
            return LightReader(sensorType, delay)
        else:
            assert 0, "Bad sensor creation: " + sensorType

    @abc.abstractmethod
    def createSensor(sensorType):
        """Retrieve data from the input source and return a Sensor object.
        @param sensorType: The kind of sensor to be created
        @type sensorType: String
        """
        pass

    @abc.abstractmethod
    def measure(self):
        pass

    def startThread(self):
        print "inside startThread"  
        self.threadSensor.start()

    def pauseThread(self):
        print "inside pauseThread" 
        #self.threadSensor.

    def releaseThread(self):
        print "inside releaseThread" 
        self.threadSensor.release()
    
    def saveData(self, valuereaded = None):
          sm = SensorMesurement(sensor_id = self.sensor_id, value = valuereaded)
          sm.save()
          
          
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
            
class LightReader(SensorReader):
    '''
    classdocs
    '''
    __metaclass__ = abc.ABCMeta

    def __init__(self, sensorName = "LDR", delay = 5, sensor_id = None, sensor_id = None):
        '''
        Constructor
        '''
        SensorReader.__init__(self, None, delay, sensor_id)
        self.sensor = LDR()
        # self.threadSensor = Thread(target = self.measureLight, args=(self.sensor, delay))
        self.threadSensor.daemon = True
    
    def measure(self):
        self.measureLight()

    def measureLight(self):
        try:
            while (True) :
                #self.sensor.getLux()         #salvar aqui no banco a leitura
                value =  self.sensor.getLux()
                self.saveData(value) 
                print ("Light: " + value + " lx")
                time.sleep(self.delay)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            traceback.print_exc() 
            print "saindo da thread"

            
class LDR(object):
    '''
    classdocs
    '''
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        '''
        Constructor
        '''
        self.setup()
    
    def setup(self):
        """
        Setup the board and GPIO  
        @return: void
        """
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.__pin = 18
        self.__lux = ""
        
    ##
    # @param pin: the GPIO pin used to wire the sensor
    # @return: void
    def changeSetup(self, pin):
        """
        @param pin: the GPIO pin used to wire the sensor.
        @return: void
        """
        self.__pin = pin
        
        
    def getLux(self):
        """Setup the GPIO."""
        return  str(5000.0 / self.__RCtime()) 

    def __RCtime (self):
        reading = 0
        GPIO.setup(self.__pin, GPIO.OUT)
        GPIO.output(self.__pin, GPIO.LOW)
        time.sleep(0.1)

        GPIO.setup(self.__pin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(self.__pin) == GPIO.LOW):
                reading += 1
        return reading

        
    def __del__(self):
        """ We're no longer using the GPIO, so tell software we're done."""
