# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-14 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forever_home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='happyending',
            name='status',
            field=models.BooleanField(default='False', verbose_name='For adoption'),
        ),
    ]