# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 00:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20170117_2207'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Marks',
        ),
        migrations.AddField(
            model_name='questions',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
