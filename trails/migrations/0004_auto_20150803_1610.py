# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0003_auto_20150803_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trail',
            name='location',
            field=models.CharField(max_length=500),
        ),
    ]
