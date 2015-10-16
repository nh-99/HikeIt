# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_trailimage_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trailimage',
            name='image',
            field=models.ImageField(upload_to=b'images'),
        ),
    ]
