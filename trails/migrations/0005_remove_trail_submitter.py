# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0004_trail_submitter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trail',
            name='submitter',
        ),
    ]
