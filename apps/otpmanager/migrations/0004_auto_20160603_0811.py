# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-03 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otpmanager', '0003_kisanuser_otp_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='msg',
            field=models.CharField(default='Hi', max_length=30),
        ),
        migrations.AddField(
            model_name='message',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]