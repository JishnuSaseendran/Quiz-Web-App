# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_questions_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='mark',
            field=models.IntegerField(default=0),
        ),
    ]