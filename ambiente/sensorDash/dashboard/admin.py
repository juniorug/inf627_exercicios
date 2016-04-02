from django.contrib import admin
from .models import Sensor, SensorFamily, Place

admin.site.register(Place)
admin.site.register(SensorFamily)
admin.site.register(Sensor)
