# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0002_auto_20150730_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trail',
            name='location',
            field=models.CharField(max_length=200),
        ),
    ]
