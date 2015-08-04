# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0004_auto_20150803_1610'),
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='trailname',
        ),
        migrations.AddField(
            model_name='image',
            name='trail',
            field=models.ForeignKey(default=None, to='trails.Trail'),
        ),
    ]
