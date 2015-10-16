# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paths', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='path',
            name='path_file',
            field=models.FileField(upload_to=b'files'),
        ),
    ]
