# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-04 05:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0006_match_status_match_teams'),
    ]

    operations = [
        migrations.AddField(
            model_name='match_status',
            name='isCalculated',
            field=models.BooleanField(default=False),
        ),
    ]
