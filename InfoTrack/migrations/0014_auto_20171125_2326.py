# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-26 04:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('InfoTrack', '0013_auto_20171101_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('username', models.CharField(help_text='Enter your name:First Name and Second Name.', max_length=20)),
                ('description', models.TextField(blank=True, help_text='Please describe yourself so other can know you.')),
                ('phone', models.IntegerField(help_text='Please enter you phone number.', null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('userid', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular user.', primary_key=True, serialize=False)),
                ('grade', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FRESHMAN', max_length=2)),
                ('major', models.CharField(help_text='Please enter your major.', max_length=20)),
            ],
            options={
                'ordering': ['username'],
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
