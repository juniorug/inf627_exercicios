import arrow
import logging
import pdb 
import traceback
from datetime import date, timedelta
from django.shortcuts import render
from .models import SensorMeasurement
from time import strptime

logger = logging.getLogger(__name__)

def dashboard(request):
    measurements = SensorMeasurement.objects.filter(
        datetime_measurement__gte=date.today()- timedelta(days = 2)
    ).order_by("datetime_measurement")


    temperature_values = SensorMeasurement.objects.filter(
        datetime_measurement__gte=date.today() - timedelta(days = 2)
    ).filter(sensor_id=1).values_list('value', flat=True).order_by('value').distinct() 
    
    temperature_values2 = SensorMeasurement.objects.filter(
        datetime_measurement__gte=date.today() - timedelta(days = 2)
    ).filter(sensor_id=1).values_list('value', 'datetime_measurement').order_by('value', 'datetime_measurement').distinct() 

    datetime_values = SensorMeasurement.objects.filter(
        datetime_measurement__gte=date.today() - timedelta(days = 2)
    ).filter(sensor_id=1).values_list('datetime_measurement', flat=True).order_by('datetime_measurement').distinct()     

    
    list_result = [entry for entry in temperature_values2]
    print (type(temperature_values2))
    #print '[%s]' % ', '.join(map(str,  temperature_values2))    
    manipulateQuerySet(temperature_values2)
    testData = thirty_day_registrations()
    print '[%s]' % ', '.join(map(str, testData))
    return render(request, 'dashboard/index.html', {
        'sensorchart': measurements,
        '30_day_registrations': testData,
        'temperature_values': getIntListValues(temperature_values),
        'temperature labels': datetime_values 
    })


# def get_context_data(self, **kwargs):
#     context = super(AnalyticsIndexView, self).get_context_data(**kwargs)
#     context['30_day_registrations'] = self.thirty_day_registrations()
#     return context


def manipulateQuerySet(list_values):
    for tuple in list_values:
        print "this is a tuple: %s" % (tuple,)
        
        
def getTimeValues(list_values):
    for i in list_values:
        t = strptime(i, '%H:%M')
        print t.tm_hour

def getIntListValues(list_values):
    list_result = [definition.encode("utf8") for definition in list_values]
    list_result = [int(i) for i in list_result]
    return list_result 

def thirty_day_registrations():
    final_data = []

    date = arrow.now()
    for day in range(1, 30):
        date = date.replace(days=-1)
        count = SensorMeasurement.objects.filter(
            datetime_measurement__gte=date.floor('day').datetime,
            datetime_measurement__lte=date.ceil('day').datetime).count()
        final_data.append(count)

    return final_data
