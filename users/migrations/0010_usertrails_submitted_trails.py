# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0003_auto_20150824_2027'),
        ('users', '0009_auto_20150824_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertrails',
            name='submitted_trails',
            field=models.ManyToManyField(related_name='submitted', to='trails.Trail'),
        ),
    ]
