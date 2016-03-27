from django.shortcuts import render
# from chartit import DataPool, Chart
from .models import SensorMesurement
import datetime


def dashboard(request):
    # measurements = SensorMesurement.objects.filter(
    #     datetime_measurement__gte=datetime.date.today()
    # ).order_by("datetime_measurement")

    # https://www.djangopackages.com/grids/g/charts/

    # http://chartit.shutupandship.com/docs/#installation
    # Step 1: Create a DataPool with the data we want to retrieve.
    # weatherdata = \
    #     DataPool(
    #         series=[{'options': {
    #             'source': SensorMesurement.objects.filter(
    #                 datetime_measurement__gte=datetime.date.today()
    #             ).order_by("datetime_measurement")},
    #             'terms': [
    #             'datetime_measurement',
    #             'value']}
    #         ])

    # # Step 2: Create the Chart object
    # cht = Chart(
    #     datasource=weatherdata,
    #     series_options=[{'options': {
    #         'type': 'line',
    #         'stacking': False},
    #         'terms': {
    #         'datetime_measurement': [
    #             'value']
    #     }}],
    #     chart_options={'title': {
    #         'text': 'Medida dos Sensores'},
    #         'xAxis': {
    #         'title': {
    #             'text': 'Datetime da medição'}}})

    # Step 3: Send the chart object to the template.
    # return render_to_response({'weatherchart': cht})

    return render(request, 'sensorDash/dashboard.html', {'sensorchart': cht})
