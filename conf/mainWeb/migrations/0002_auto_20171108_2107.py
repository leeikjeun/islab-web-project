# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-08 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainWeb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='userImg',
            field=models.FileField(default='test/None/no-img.jpg', upload_to='test/%m/%d'),
        ),
    ]