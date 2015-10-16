# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20150825_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertrails',
            name='submitted_trails',
        ),
    ]
