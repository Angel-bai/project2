# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-07 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='data_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]