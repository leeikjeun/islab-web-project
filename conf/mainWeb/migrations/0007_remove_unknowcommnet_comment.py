# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-09 14:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainWeb', '0006_auto_20171109_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unknowcommnet',
            name='comment',
        ),
    ]