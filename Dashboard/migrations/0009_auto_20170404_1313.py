# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-04 07:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0008_points_scored'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match_status',
            name='id',
        ),
        migrations.RemoveField(
            model_name='overall_status',
            name='id',
        ),
        migrations.AlterField(
            model_name='match_status',
            name='match_number',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='overall_status',
            name='akash',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
