# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('togetthereApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sp',
            old_name='address',
            new_name='sp_address',
        ),
    ]
