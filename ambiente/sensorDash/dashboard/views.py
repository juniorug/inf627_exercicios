import datetime
import arrow
from django.shortcuts import render
from .models import SensorMeasurement


def dashboard(request):
    measurements = SensorMesurement.objects.filter(
        datetime_measurement__gte=datetime.date.today()
    ).order_by("datetime_measurement")

    testData = thirty_day_registrations()
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
        count = SensorMesurement.objects.filter(
            datetime_measurement__gte=date.floor('day').datetime,
            datetime_measurement__lte=date.ceil('day').datetime).count()
        final_data.append(count)

    return final_data
