import abc
import time
import traceback
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


hr  = SensorReader.createReader('Temperature', 'DHT11Temperature')
try:
    hr.startThread()
except:
    print "saindo do main"
    traceback.print_exc()

while (True):
    time.sleep(1)
