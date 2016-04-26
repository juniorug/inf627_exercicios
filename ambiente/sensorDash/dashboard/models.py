from datetime import date, datetime
from django.db import models
from django.utils.translation import gettext as _
from reader import SensorReader
# from django.utils import timezone


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
        readerType = SensorFamily.objects.get(
            self.sensor_family_id).values('family_name')
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
