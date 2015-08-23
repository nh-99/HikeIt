# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0001_initial'),
        ('users', '0006_auto_20150819_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertrails',
            name='completed_trails',
            field=models.ManyToManyField(related_name='completed', to='trails.Trail'),
        ),
        migrations.AlterField(
            model_name='usertrails',
            name='liked_trails',
            field=models.ManyToManyField(related_name='liked', to='trails.Trail'),
        ),
    ]
