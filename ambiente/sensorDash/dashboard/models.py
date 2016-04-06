from django.db import models
# from django.utils import timezone


class SensorFamily(models.Model):

    family_name = models.CharField(max_length=45, blank=True)
    default_measure_unit = models.CharField(max_length=45, blank=True)

    def __str__(self):
        return self.family_name


class Sensor(models.Model):

    sensor_family = models.ForeignKey('SensorFamily')
    sensor_type = models.CharField(max_length = 45)
    place = models.ForeignKey('Place')
    sampling_time = models.IntegerField(default = 1)
    pin = models.IntegerField(default = 0)
    status = models.CharField(max_length = 45)

    def __str__(self):
        return self.sensor_type + ' - ' + self.status

    def save(self, *args, **kwargs):
        super(Sensor, self).save(*args, **kwargs)
        # print self.sensor_type


class Place(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class SensorMeasurement(models.Model):

    sensor = models.ForeignKey('Sensor')
    datetime_measurement = models.DateTimeField()
    value = models.CharField(max_length=45)

    def __str__(self):
        return self.value + ' at ' + unicode(self.datetime_measurement)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        self.datetime_measurement = timezone.now()
        return super(User, self).save(*args, **kwargs)



