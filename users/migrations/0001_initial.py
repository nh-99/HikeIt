# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HikeItUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('username', models.CharField(unique=True, max_length=254, blank=True)),
                ('first_name', models.CharField(max_length=30, blank=True)),
                ('last_name', models.CharField(max_length=30, blank=True)),
                ('email', models.EmailField(unique=True, max_length=254, blank=True)),
                ('role', models.CharField(default=b'member', max_length=30)),
                ('image', models.CharField(max_length=200, blank=True)),
                ('token', models.CharField(max_length=300, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
