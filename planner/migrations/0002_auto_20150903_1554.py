# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0006_trail_submitter'),
        ('planner', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planner',
            name='trail',
        ),
        migrations.AddField(
            model_name='planner',
            name='trail',
            field=models.ManyToManyField(to='trails.Trail'),
        ),
    ]
