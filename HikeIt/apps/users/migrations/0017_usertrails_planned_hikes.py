# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0005_auto_20151225_0604'),
        ('users', '0016_usertrails_saved_trails'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertrails',
            name='planned_hikes',
            field=models.ManyToManyField(related_name='planned_hikes', to='planner.Planner'),
        ),
    ]
