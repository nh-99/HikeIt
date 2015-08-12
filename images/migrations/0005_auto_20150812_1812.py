# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_auto_20150812_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='lat',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='long',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
