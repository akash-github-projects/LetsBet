# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-03 07:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0002_auto_20170403_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='match_status',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
