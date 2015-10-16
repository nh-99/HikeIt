# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trails', '0005_remove_trail_submitter'),
    ]

    operations = [
        migrations.AddField(
            model_name='trail',
            name='submitter',
            field=models.ForeignKey(related_name='submitter', default=None, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
