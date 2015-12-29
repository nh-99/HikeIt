# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_usertrails_timeline_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertrails',
            name='timeline_token',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
