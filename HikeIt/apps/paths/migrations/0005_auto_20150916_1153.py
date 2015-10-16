# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paths', '0004_auto_20150916_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='path',
            name='path_file',
            field=models.FileField(upload_to=b'paths'),
        ),
    ]
