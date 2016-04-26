# import arrow
import logging
# import pdb
# import traceback
from datetime import date, timedelta
from django.shortcuts import render
from .models import SensorMeasurement
from .forms import DateRangeForm
# from time import strptime
from django.http import JsonResponse

logger = logging.getLogger(__name__)


def dashboardData(request):
    sense_values = []
    for i in range(0, 3):

        values_measured = SensorMeasurement.objects.filter(
            date_measurement__day=date.today().day
        ).filter(sensor_id=(i + 1)).values_list('value', 'time_measurement')\
            .order_by('time_measurement').distinct()[:7]
        sense_values.append(values_measured)

    tuple_list_temperature_value = getListsFromToupleLists(sense_values[0])
    tuple_list_humidity_value = getListsFromToupleLists(sense_values[1])
    tuple_list_luminosity_value = getListsFromToupleLists(sense_values[2])

    return JsonResponse({
        'chart_labels': tuple_list_temperature_value[1],
        'temperature_values': tuple_list_temperature_value[0],
        'humidity_values': tuple_list_humidity_value[0],
        'luminosity_values': tuple_list_luminosity_value[0]
    })


def dashboard(request):
    sense_values = []
    if request.method == "POST":
        print request.POST
        print request.POST['initialDate']

    for i in range(0, 3):

        values_measured = SensorMeasurement.objects.filter(
            date_measurement__day=date.today().day
        ).filter(sensor_id=(i + 1)).values_list('value', 'time_measurement')\
            .order_by('time_measurement').distinct()[:7]
        sense_values.append(values_measured)

    tuple_list_temperature_value = getListsFromToupleLists(sense_values[0])
    tuple_list_humidity_value = getListsFromToupleLists(sense_values[1])
    tuple_list_luminosity_value = getListsFromToupleLists(sense_values[2])

    return render(request, 'dashboard/index.html', {
        'chart_labels': tuple_list_temperature_value[1],
        'temperature_values': tuple_list_temperature_value[0],
        'humidity_values': tuple_list_humidity_value[0],
        'luminosity_values': tuple_list_luminosity_value[0]
    })


def getListsFromToupleLists(toupleList):
    list_keys = []
    list_values = []
    for tuple in toupleList:
        list_keys.append(getStringValue(tuple[0]))
        list_values.append(getStringTimeValue(tuple[1]))
    print(type(list_keys))
    print '[%s]' % ', '.join(map(str,  list_keys))
    print(type(list_values))
    print '[%s]' % ', '.join(map(str,  list_values))
    return (list_keys, list_values)


def getStringValue(value):
    return value.encode("utf8")


def getIntValue(value):
    return int(value.encode("utf8"))


def getStringDateValue(dateValue):
    return dateValue.strftime("%d/%m/%Y").encode("utf8")


def getStringTimeValue(timeValue):
    return timeValue.strftime("%H:%M:%S").encode("utf8")

'''
def thirty_day_registrations():
    final_data = []

    date = arrow.now()
    for day in range(1, 30):
        date = date.replace(days=-1)
        count = SensorMeasurement.objects.filter(
            date_measurement__gte=date.floor('day').datetime,
            date_measurement__lte=date.ceil('day').datetime).count()
        final_data.append(count)

    return final_data

def getTimeValues(list_values):
    for i in list_values:
        t = strptime(i, '%H:%M')
        print t.tm_hour

def getIntListValues(list_values):
    list_result = [definition.encode("utf8") for definition in list_values]
    list_result = [int(i) for i in list_result]
    return list_result 

def getListValues(list_values):
    list_result = [definition.encode("utf8") for definition in list_values]
    list_result = [str(i) for i in list_result]
    return list_result 

def get_context_data(self, **kwargs):
    context = super(AnalyticsIndexView, self).get_context_data(**kwargs)
    context['30_day_registrations'] = self.thirty_day_registrations()
    return context


def manipulateQuerySet(list_values):
    list_tuple_aux = []
    for tuple in list_values:
        value = tuple[0]
        time =  tuple[1] 
        tuple_aux = (value, time)
        list_tuple_aux.append(tuple_aux) 
    return list_tuple_aux'''
