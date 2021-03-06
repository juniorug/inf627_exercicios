from django.db import models
from django.utils.translation import gettext as _

import abc
import time
import traceback
import RPi.GPIO as GPIO, os
from concretefactory.humiditySensorFactory import HumiditySensorFactory
from concretefactory.temperatureSensorFactory import TemperatureSensorFactory
from datetime import date,datetime,timedelta
from threading import *


# from django.utils import timezone

#from django.conf import settings
#if not settings.configured:
#    settings.configure("sensorDash.settings", DEBUG=True)


class SensorFamily(models.Model):

    family_name = models.CharField(max_length=45, blank=True)
    default_measure_unit = models.CharField(max_length=45, blank=True)

    def __str__(self):
        return self.family_name


class Sensor(models.Model):

    sensor_family = models.ForeignKey('SensorFamily')
    sensor_type = models.CharField(max_length=45)
    place = models.ForeignKey('Place')
    sampling_time = models.IntegerField(default=1)
    pin = models.IntegerField(default=0)
    status = models.CharField(max_length=45)

    def __str__(self):
        return self.sensor_type + ' - ' + self.status

    def save(self, *args, **kwargs):
        super(Sensor, self).save(*args, **kwargs)

        # Identify the sensor and call it's reader thread
        print self.sensor_family_id
        print self.sensor_family

        readerType = SensorFamily.objects.get(
            id=self.sensor_family_id).family_name
        reader = SensorReader.createReader(
            readerType, self.sensor_type, self.sampling_time, self.id)
        reader.startThread()


class Place(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class SensorMeasurement(models.Model):

    sensor = models.ForeignKey('Sensor')
    date_measurement = models.DateField(_("Date"), default=date.today)
    time_measurement = models.TimeField(blank=True, null=True)
    value = models.CharField(max_length=45)

    def __str__(self):
        return self.value + ' at ' + unicode(self.date_measurement)\
            + ' ' + unicode(self.time_measurement)

    # def save(self, *args, **kwargs):
    #     ''' On save, update timestamps '''
    #     self.datetime_measurement = timezone.now()
    #     return super(User, self).save(*args, **kwargs)
#!/usr/bin/env python

import abc
import time
import traceback
import RPi.GPIO as GPIO, os
from concretefactory.humiditySensorFactory import HumiditySensorFactory
from concretefactory.temperatureSensorFactory import TemperatureSensorFactory
from datetime import date,datetime,timedelta
from threading import *
from models import SensorMeasurement

#from models import SensorMesurement



class SensorReader(object):
    '''
    classdocs
    '''
    __metaclass__ = abc.ABCMeta

    def __init__(self, sensor = None, delay = 5, sensor_id = None):
        '''
        Constructor
        '''
        self.event = Event()
        self.event.set()
        self.threadSensor = Thread(target = self.measure, args=())
        self.sensor = sensor
        self.delay = delay
        self.sensor_id = sensor_id
        self.filename = ""

    @staticmethod
    def createReader(readerType, sensorType, delay, sensor_id):

        if (readerType == 'Temperature'):
            return TemperatureReader(sensorType, delay, sensor_id)
        elif(readerType == 'Humidity'):
            return HumidityReader(sensorType, delay, sensor_id)
        elif(readerType == 'Luminosity'):
            return LightReader(sensorType, delay, sensor_id)
        else:
            assert 0, "Bad sensor creation: " + sensorType


    @abc.abstractmethod
    def measure(self):
        pass

    def startThread(self):
        self.threadSensor.start()

    def pauseThread(self):
        self.event.clear()
        print("inside pauseThread.")

    def releaseThread(self):
        print("inside releaseThread.")
        self.event.set()
        self.threadSensor = Thread(target = self.measure, args=())
        self.threadSensor.daemon = True
        self.threadSensor.start()
    
    def saveData(self, valuereaded = None):
        #sm = SensorMesurement(sensor_id = self.sensor_id, value = valuereaded)
        #sm.save()
        #print ("saving. should save in the database")
        #pass
        if (valuereaded is not None):

            sm = SensorMeasurement(value = valuereaded, sensor_id = self.sensor_id, date_measurement = date.today(),time_measurement = datetime.now().strftime('%H:%M:%S'))
            sm.save()
            #str_insert = "INSERT INTO dashboard_sensormeasurement (sensor_id,value, date_measurement,time_measurement) VALUES ({}, '{}', '{}', '{}');\n".format(self.sensor_id, valuereaded, date.today(), datetime.now().strftime('%H:%M:%S'))
            
            #file = open(self.filename, "a+")
            #file.write(str_insert)
            #file.close()
   
          
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
        self.sensor = TemperatureSensorFactory.createSensor(sensorName)
        self.sensor.changeSetup(4)
        # self.threadSensor = Thread(target = self.measureTemperature, args=(self.sensor,delay))
        self.threadSensor.daemon = True
        self.filename = "temperature.txt"

    def measure(self):
        self.measureTemperature()
        
    def measureTemperature(self):
        try:
            #while (True) :
            while (self.event.isSet()):       
                value = self.sensor.getTemperature()
                self.saveData(value)             #salvar aqui no banco a leitura
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

    def __init__(self, sensorName = "DHT11Humidity", delay = 5, sensor_id = None):
        '''
        Constructor
        '''
        SensorReader.__init__(self, None, delay, sensor_id)
        self.sensor = HumiditySensorFactory.createSensor(sensorName)
        self.sensor.changeSetup(4)
        # self.threadSensor = Thread(target = self.measureHumidity, args=(self.sensor, delay))
        self.threadSensor.daemon = True
        self.filename = "humidity.txt"
        
    def measure(self):
        self.measureHumidity()

    def measureHumidity(self):
        try:
            #while (True) :
            while (self.event.isSet()):
                value = self.sensor.getHumidity()         
                self.saveData(value)      #salvar aqui no banco a leitura
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

    def __init__(self, sensorName = "LDR", delay = 5, sensor_id = None):
        '''
        Constructor
        '''
        SensorReader.__init__(self, None, delay, sensor_id)
        self.sensor = LDR()
        # self.threadSensor = Thread(target = self.measureLight, args=(self.sensor, delay))
        self.threadSensor.daemon = True
        self.filename = "light.txt"
    
    def measure(self):
        self.measureLight()

    def measureLight(self):
        try:
            #while (True) :
            while (self.event.isSet()):
                value =  self.sensor.getLux()
                self.saveData(value)          #salvar aqui no banco a leitura
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


