# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_usertrails_submitted_trails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertrails',
            name='submitted_trails',
        ),
    ]
