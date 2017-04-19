# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 20:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_catbreed'),
    ]

    operations = [
        migrations.CreateModel(
            name='HockeyPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=50)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.HockeyTeam')),
            ],
        ),
    ]
