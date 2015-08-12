# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images', '0002_auto_20150803_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='user',
            field=models.ForeignKey(related_name='+', default=None, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='trail',
            field=models.ForeignKey(to='trails.Trail'),
        ),
    ]
