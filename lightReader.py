#!/usr/bin/env python

import abc
import time
import traceback
import RPi.GPIO as GPIO, os
from threading import Thread

class LightReader(object):
    '''
    classdocs
    '''
    __metaclass__ = abc.ABCMeta

    def __init__(self, sensorName="LDR"):
        '''
        Constructor
        '''
        self.sensor = LDR()
        self.threadSensor = Thread(target = self.measureLight, args=(self.sensor,5))
        self.threadSensor.daemon = True

    def startThread(self):
        self.threadSensor.start()

    def pauseThread(self):
        print "inside pauseThread" 
        #self.threadSensor.

    def releaseThread(self):
        print "inside releaseThread" 
        self.threadSensor.release()
        
    def measureLight(self,sensor, delay):
        try:
            while (True) :
                #self.sensor.getLux()         #salvar aqui no banco a leitura
                print ("Light: " + self.sensor.getLux() + " lx")
                time.sleep(delay)
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



hr = LightReader()
try:
    hr.startThread()
except:
    print "saindo do main"
    traceback.print_exc()

while (True):
    time.sleep(1)
    