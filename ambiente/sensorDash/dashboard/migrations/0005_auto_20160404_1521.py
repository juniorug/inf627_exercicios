# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 18:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_sensor_pin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensormesurement',
            old_name='sensor_id',
            new_name='sensor',
        ),
    ]
