# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('togetthereApp', '0009_auto_20150425_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sp',
            name='category',
            field=models.CharField(max_length=45, choices=[(b'medical', b'Medical'), (b'restaurants', b'Restaurants'), (b'shopping', b'Shopping'), (b'public_services', b'Public Services'), (b'transportation', b'Transportation'), (b'help', b'Help')]),
        ),
    ]
