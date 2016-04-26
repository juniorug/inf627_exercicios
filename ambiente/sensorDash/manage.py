# #!/usr/bin/env python
# import os
# import sys

# if __name__ == "__main__":
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sensorDash.settings")

#     from django.core.management import execute_from_command_line

#     execute_from_command_line(sys.argv)

import os
import sys
from reader.reader.py import SensorReader
from dashboard.models.py import Sensor

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sensorDash.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

    if ('runserver' in sys.argv):
        sensor_reader_list = []
        sensor_set = Sensor.objects.filter(
            status='ON').select_related('sensor_family__family_name')

        for sensor in sensor_set:
            sensor_reader_list.append(SensorReader.createReader(
                sensor.family_name, sensor.sensor_type,
                sensor.sampling_time, sensor.id))

        try:
            for reader in sensor_reader_list:
                reader.startThread()

        except (KeyboardInterrupt, SystemExit):
            raise

        except:
            print "saindo do main"
            traceback.print_exc()
