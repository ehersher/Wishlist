# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2019-02-22 03:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_book_is_selected'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='is_selected',
        ),
    ]
