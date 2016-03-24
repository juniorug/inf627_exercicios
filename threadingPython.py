#!/usr/bin/env python

import abc
import time
#from concretefactory.humiditySensorFactory import HumididtySensorFactory
from threading import Thread

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
		
		
def measureHumidity(sensor, delay):
    try:
        while (True) :
            sensor.getHumidity()	 #salvar aqui no banco a leitura
            time.sleep(delay)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:	
        print "saindo da thread"

#dht11 = HumididtySensorFactory.createSensor("DHT11Humididty")
dht11 = Sensor()
try:
    t = Thread(target=measureHumidity, args=(dht11,5))
    t.daemon = True
    t.start()
except:
    print "saindo do main"

while (True):
    time.sleep(1)
        
