# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-14 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gti', '0016_auto_20180423_0203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeout', models.CharField(max_length=200)),
            ],
        ),
    ]
