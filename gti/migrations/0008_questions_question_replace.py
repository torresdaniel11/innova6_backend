# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-01 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gti', '0007_auto_20180330_0622'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='question_replace',
            field=models.BooleanField(default=False),
        ),
    ]