# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('togetthereApp', '0005_auto_20150424_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='sp',
            name='city',
            field=models.CharField(default='', max_length=225, db_index=True),
            preserve_default=False,
        ),
    ]
