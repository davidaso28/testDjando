# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 03:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0003_auto_20170621_2158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascota',
            name='vacuna',
        ),
    ]
