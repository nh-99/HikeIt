# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0006_trail_submitter'),
        ('users', '0015_remove_usertrails_submitted_trails'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertrails',
            name='saved_trails',
            field=models.ManyToManyField(related_name='saved', to='trails.Trail'),
        ),
    ]
