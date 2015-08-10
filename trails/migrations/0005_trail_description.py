# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0004_auto_20150803_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='trail',
            name='description',
            field=models.CharField(default=b'No description found', max_length=500),
        ),
    ]
