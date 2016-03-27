# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 18:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_type', models.CharField(max_length=45)),
                ('status', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='SensorFamily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_name', models.CharField(blank=True, max_length=45)),
                ('default_measure_unit', models.CharField(blank=True, max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='SensorMesurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_measurement', models.DateTimeField(auto_now=True)),
                ('value', models.CharField(max_length=45)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensorDash.Place')),
                ('sensor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensorDash.Sensor')),
            ],
        ),
        migrations.AddField(
            model_name='sensor',
            name='sensor_family_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensorDash.SensorFamily'),
        ),
    ]
