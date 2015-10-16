# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150818_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertrails',
            name='liked_trails',
            field=models.ManyToManyField(to='trails.Trail', null=True, blank=True),
        ),
    ]
