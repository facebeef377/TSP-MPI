# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-20 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_id', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('cityCount', models.IntegerField()),
                ('graph', models.TextField(max_length=40000)),
                ('time', models.CharField(max_length=200)),
                ('population', models.IntegerField()),
                ('generations', models.IntegerField()),
                ('wpz', models.IntegerField()),
                ('proc', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='proc',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='wpz',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
