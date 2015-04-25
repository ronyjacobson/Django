# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('togetthereApp', '0004_auto_20150424_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sp',
            name='latitude',
            field=models.DecimalField(db_index=True, null=True, max_digits=7, decimal_places=7, blank=True),
        ),
        migrations.AlterField(
            model_name='sp',
            name='longitude',
            field=models.DecimalField(db_index=True, null=True, max_digits=7, decimal_places=7, blank=True),
        ),
    ]
