# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trail',
            name='approved',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
