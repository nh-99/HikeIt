# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_usertrails_planned_hikes'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertrails',
            name='timeline_token',
            field=models.CharField(default=None, max_length=150, null=True),
        ),
    ]
