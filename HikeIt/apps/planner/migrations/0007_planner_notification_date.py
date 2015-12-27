# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0006_auto_20151225_0648'),
    ]

    operations = [
        migrations.AddField(
            model_name='planner',
            name='notification_date',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
