# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('togetthereApp', '0002_auto_20150424_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 24, 14, 38, 15, 28000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sp',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
