# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0006_trail_submitter'),
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='trail',
        ),
        migrations.AddField(
            model_name='issue',
            name='trail',
            field=models.ForeignKey(default=None, to='trails.Trail'),
            preserve_default=False,
        ),
    ]
