# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-30 04:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gti', '0004_auto_20180330_0357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='questionrecords',
            name='question_record_conversation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gti.Conversations'),
        ),
        migrations.AlterField(
            model_name='questionrecords',
            name='question_record_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='gti.Questions'),
        ),
    ]