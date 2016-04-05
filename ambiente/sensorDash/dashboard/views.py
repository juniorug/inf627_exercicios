import arrow
import logging
import pdb 
import traceback
from datetime import date, timedelta
from django.shortcuts import render
from .models import SensorMeasurement

logger = logging.getLogger(__name__)

def dashboard(request):
    measurements = SensorMeasurement.objects.filter(
        datetime_measurement__gte=date.today()- timedelta(days = 1)
    ).order_by("datetime_measurement")


    temperature_values = SensorMeasurement.objects.filter(
        datetime_measurement__gte=date.today() - timedelta(days = 1)
    ).filter(sensor_id=1).values_list('value', flat=True).order_by('value').distinct()   

    list_result = [entry for entry in temperature_values]
    print (type(list_result))
    print '[%s]' % ', '.join(map(str, list_result))
    #traceback.print_exc()
    #pdb.set_trace()

    testData = thirty_day_registrations()
    print '[%s]' % ', '.join(map(str, testData))
    return render(request, 'dashboard/index.html', {
        'sensorchart': measurements,
        '30_day_registrations': testData
    })


# def get_context_data(self, **kwargs):
#     context = super(AnalyticsIndexView, self).get_context_data(**kwargs)
#     context['30_day_registrations'] = self.thirty_day_registrations()
#     return context


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
