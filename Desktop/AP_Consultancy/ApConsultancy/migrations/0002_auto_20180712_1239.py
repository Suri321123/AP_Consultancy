# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-12 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApConsultancy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeruser',
            name='emailId',
            field=models.EmailField(max_length=100),
        ),
    ]
