# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_review_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='approved',
        ),
    ]
