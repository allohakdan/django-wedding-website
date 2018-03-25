# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-22 00:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0016_party_rehearsal_dinner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='guests.Party'),
        ),
    ]
