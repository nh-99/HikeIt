# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trails', '0003_auto_20150824_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='trail',
            name='submitter',
            field=models.OneToOneField(null=True, default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
