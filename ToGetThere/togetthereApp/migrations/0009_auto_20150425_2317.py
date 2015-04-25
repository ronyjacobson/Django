# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('togetthereApp', '0008_auto_20150425_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='sp',
            name='rank',
            field=models.BigIntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='sp',
            name='voters',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='likes',
            field=models.IntegerField(default=0, db_index=True, blank=True),
        ),
    ]
