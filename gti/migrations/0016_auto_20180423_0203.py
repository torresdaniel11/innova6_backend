# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-23 02:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gti', '0015_auto_20180423_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='article_url',
            field=models.TextField(blank=True, null=True),
        ),
    ]