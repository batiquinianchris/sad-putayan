# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-08 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=120, verbose_name='Section Name')),
                ('status', models.IntegerField(verbose_name='Status')),
            ],
        ),
    ]