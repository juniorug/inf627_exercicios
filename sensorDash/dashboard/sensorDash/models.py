from django.db import models
# from django.utils import timezone


class SensorFamily(models.Model):

    family_name = models.CharField(max_length=45, blank=True)
    default_measure_unit = models.CharField(max_length=45, blank=True)

    def __str__(self):
        return self.family_name


class Sensor(models.Model):

    sensor_family_id = models.ForeignKey('SensorFamily')
    sensor_type = models.CharField(max_length=45)
    status = models.CharField(max_length=45)

    def __str__(self):
        return self.sensor_type + ' - ' + self.status


class Place(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class SensorMesurement(models.Model):

    sensor_id = models.ForeignKey('Sensor')
    place = models.ForeignKey('Place')
    datetime_measurement = models.DateTimeField(auto_now=True)
    value = models.CharField(max_length=45)

    def __str__(self):
        return self.place + ': ' + self.value + ' at ' + self.datetime_measurement
