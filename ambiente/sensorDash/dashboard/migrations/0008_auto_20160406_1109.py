# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-06 14:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20160404_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensormeasurement',
            name='datetime_measurement',
        ),
        migrations.AddField(
            model_name='sensormeasurement',
            name='date_measurement',
            field=models.DateField(default=datetime.date.today, verbose_name=b'Date'),
        ),
        migrations.AddField(
            model_name='sensormeasurement',
            name='time_measurement',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
