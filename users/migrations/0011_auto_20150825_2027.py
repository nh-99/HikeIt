# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0003_auto_20150824_2027'),
        ('users', '0010_usertrails_submitted_trails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertrails',
            name='submitted_trails',
        ),
        migrations.AddField(
            model_name='usertrails',
            name='submitted_trails',
            field=models.OneToOneField(related_name='submitted', default=None, to='trails.Trail'),
        ),
    ]
