# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 19:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20160404_1525'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SensorMesurement',
            new_name='SensorMeasurement',
        ),
    ]
