# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0006_trail_submitter'),
        ('planner', '0004_planneroptions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planneroptions',
            name='planner',
        ),
        migrations.RemoveField(
            model_name='planner',
            name='user',
        ),
        migrations.RemoveField(
            model_name='planner',
            name='trail',
        ),
        migrations.AddField(
            model_name='planner',
            name='trail',
            field=models.ForeignKey(default=None, to='trails.Trail'),
        ),
        migrations.DeleteModel(
            name='PlannerOptions',
        ),
    ]
