# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0007_planner_notification_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planner',
            name='completed',
        ),
    ]
