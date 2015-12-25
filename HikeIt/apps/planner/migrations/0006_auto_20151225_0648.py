# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0005_auto_20151225_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planner',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
