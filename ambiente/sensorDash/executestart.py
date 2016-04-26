from dashboard.models import SensorReader
from dashboard.models import Sensor
from dashboard.models import SensorFamily


sensor_reader_list = []
sensor_set = Sensor.objects.filter(status = 'ON').select_related('sensor_family__family_name')

for sensor in sensor_set:

    family = SensorFamily.objects.get(id = sensor.sensor_family)
    sensor_reader_list.append(SensorReader.createReader(family.family_name, sensor.sensor_type, sensor.sampling_time, sensor.id))

try:
    for reader in sensor_reader_list:
        reader.startThread()

except (KeyboardInterrupt, SystemExit):
    raise

except:
    print "saindo do main"
    traceback.print_exc()
