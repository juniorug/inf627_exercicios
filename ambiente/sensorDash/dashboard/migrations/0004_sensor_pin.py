# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20160404_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='pin',
            field=models.IntegerField(default=0),
        ),
    ]
