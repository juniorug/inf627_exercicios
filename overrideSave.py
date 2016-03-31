from sensorReader import sensorReader


def save(self,*args,**kwargs):
    super(Sensor,self).save(*args,**kwargs)
    # readerType = "select family_name from sensor_family where id = self.sensor_family_id;" # precisa fazer essa consulta
    readerType = SensorFamily.objects.get(self.sensor_family_id).values('family_name')
    reader = SensorReader.createReader(readerType, self.sensor_type, self.sampling_time)


