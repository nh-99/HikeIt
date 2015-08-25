# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20150825_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertrails',
            name='submitted_trails',
            field=models.OneToOneField(related_name='submitted', null=True, default=None, to='trails.Trail'),
        ),
    ]
