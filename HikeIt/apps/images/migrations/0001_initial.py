# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trails', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrailImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lat', models.FloatField(null=True, blank=True)),
                ('long', models.FloatField(null=True, blank=True)),
                ('image', models.FileField(upload_to=b'images')),
                ('trail', models.ForeignKey(to='trails.Trail')),
                ('user', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
