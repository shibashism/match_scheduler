# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-16 18:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_sportsspecification'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SportsSpecification',
        ),
    ]