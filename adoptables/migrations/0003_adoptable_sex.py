# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-09 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptables', '0002_adoptable_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoptable',
            name='sex',
            field=models.CharField(default='', max_length=100),
        ),
    ]