# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-09 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainWeb', '0011_auto_20171110_0312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='messages',
        ),
        migrations.AddField(
            model_name='message',
            name='receiveUser',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
