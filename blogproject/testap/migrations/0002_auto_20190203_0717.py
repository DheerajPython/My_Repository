# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-03 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testap', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publish',)},
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('dratf', 'DRAFT'), ('publish', 'PUBLISHED')], default='draft', max_length=10),
        ),
    ]
