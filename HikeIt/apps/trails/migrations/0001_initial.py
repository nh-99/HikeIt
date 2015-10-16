# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
                ('difficulty', models.CharField(max_length=50)),
                ('distance', models.FloatField()),
                ('location', models.CharField(max_length=500)),
                ('description', models.CharField(default=b'No description found', max_length=500)),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
    ]
