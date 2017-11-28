# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 19:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('InfoTrack', '0006_auto_20171031_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]