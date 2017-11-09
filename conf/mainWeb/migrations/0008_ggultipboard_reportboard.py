# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-09 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainWeb', '0007_remove_unknowcommnet_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='GGulTipBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('user', models.CharField(blank=True, max_length=50)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('content', models.TextField()),
                ('fileContent', models.FileField(blank=True, default=None, null=True, upload_to='boardFile/%m/%d')),
                ('professor', models.CharField(blank=True, max_length=50)),
                ('hit_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ReportBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('user', models.CharField(blank=True, max_length=50)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('content', models.TextField()),
                ('fileContent', models.FileField(blank=True, default=None, null=True, upload_to='boardFile/%m/%d')),
                ('professor', models.CharField(blank=True, max_length=50)),
                ('hit_count', models.IntegerField(default=0)),
            ],
        ),
    ]
