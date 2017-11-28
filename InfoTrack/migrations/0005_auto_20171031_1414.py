# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 18:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InfoTrack', '0004_auto_20171031_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='user',
            name='post',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='InfoTrack.Post'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='InfoTrack.Post'),
        ),
    ]