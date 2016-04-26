# #!/usr/bin/env python
# import os
# import sys

# if __name__ == "__main__":
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sensorDash.settings")

#     from django.core.management import execute_from_command_line

#     execute_from_command_line(sys.argv)

import os
import sys
#from reader.reader.py import SensorReader

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sensorDash.settings")
	

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

#    from reader.reader import SensorReader	
    from dashboard.models import SensorReader
    from dashboard.models import Sensor
    from dashboard.models import SensorFamily	
    if ('runserver' in sys.argv):
	sensor_reader_list = []
        sensor_set = Sensor.objects.filter(
            status='ON').select_related('sensor_family__family_name')
	
	print sensor_set
        for sensor in sensor_set:
            print sensor.sensor_type
 #           print ("sensor famyly id: " + sensor.sensor_family) 
 #           family = SensorFamily.objects.get(id= sensor.sensor_family)
#	    print("famyly:" + family)
            sensor_reader_list.append(SensorReader.createReader(
                sensor.sensor_family.family_name, sensor.sensor_type,
                sensor.sampling_time, sensor.id))
	
        try:
            for reader in sensor_reader_list:
                reader.startThread()

        except (KeyboardInterrupt, SystemExit):
            raise

        except:
            print "saindo do main"
            traceback.print_exc()


