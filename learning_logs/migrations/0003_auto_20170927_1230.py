# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 12:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='data_added',
            new_name='date_added',
        ),
    ]
