# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0005_remove_trail_submitter'),
        ('users', '0013_remove_usertrails_submitted_trails'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertrails',
            name='submitted_trails',
            field=models.ForeignKey(related_name='submitted', default=None, to='trails.Trail', null=True),
        ),
    ]
