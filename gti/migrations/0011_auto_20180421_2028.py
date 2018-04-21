# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-21 20:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gti', '0010_auto_20180421_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluateConversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluate_conversation_score', models.CharField(max_length=200)),
                ('evaluate_conversation_observation', models.TextField()),
                ('evaluate_conversation_conversation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gti.Conversations')),
            ],
        ),
        migrations.AddField(
            model_name='questions',
            name='question_evaluate_one',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='questions',
            name='question_evaluate_two',
            field=models.BooleanField(default=False),
        ),
    ]