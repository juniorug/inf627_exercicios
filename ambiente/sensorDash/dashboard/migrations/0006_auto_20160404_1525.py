# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20160404_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensormesurement',
            name='datetime_measurement',
            field=models.DateTimeField(),
        ),
    ]
