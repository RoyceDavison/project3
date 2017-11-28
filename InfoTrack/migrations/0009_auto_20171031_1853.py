# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfoTrack', '0008_auto_20171031_1529'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['username']},
        ),
        migrations.RenameField(
            model_name='user',
            old_name='userName',
            new_name='username',
        ),
        migrations.AddField(
            model_name='post',
            name='grade',
            field=models.CharField(choices=[('---', '---'), ('clubinfo', 'ClubInfo'), ('courseinfo', 'CourseInfo'), ('lookforride', 'FreeRide'), ('tutor', 'TutorInfo'), ('rent', 'RentInfo')], default='---', max_length=10),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, help_text='Your post title.', max_length=20),
        ),
    ]
