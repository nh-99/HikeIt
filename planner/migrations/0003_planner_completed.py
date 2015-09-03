# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_auto_20150903_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='planner',
            name='completed',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
