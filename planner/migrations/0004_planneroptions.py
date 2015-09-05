# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0003_planner_completed'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlannerOptions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weather', models.BooleanField()),
                ('tide', models.BooleanField()),
                ('moon', models.BooleanField()),
                ('planned', models.BooleanField()),
                ('completed', models.BooleanField()),
                ('planner', models.OneToOneField(to='planner.Planner')),
            ],
        ),
    ]
