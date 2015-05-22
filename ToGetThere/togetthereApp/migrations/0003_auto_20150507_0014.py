# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('togetthereApp', '0002_auto_20150507_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='city_name',
            field=models.CharField(unique=True, max_length=50, db_index=True),
        ),
        migrations.AlterUniqueTogether(
            name='street',
            unique_together=set([('city', 'street_name')]),
        ),
    ]
