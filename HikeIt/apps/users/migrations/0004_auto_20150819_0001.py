# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150818_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertrails',
            name='liked_trails',
            field=models.ManyToManyField(related_name='liked_trails', null=True, to='trails.Trail', blank=True),
        ),
    ]
