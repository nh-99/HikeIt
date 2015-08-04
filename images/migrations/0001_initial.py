# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trailname', models.CharField(max_length=100)),
                ('lat', models.FloatField(default=None)),
                ('long', models.FloatField(default=None)),
                ('image', models.FileField(upload_to=b'images')),
            ],
        ),
    ]
