# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-09 09:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainWeb', '0004_unknownboard'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnknowCommnet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=50)),
                ('content', models.CharField(blank=True, max_length=100)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainWeb.UnknownBoard')),
            ],
        ),
    ]
