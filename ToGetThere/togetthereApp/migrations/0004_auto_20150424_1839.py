# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('togetthereApp', '0003_auto_20150424_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sp',
            name='category',
            field=models.CharField(blank=True, max_length=45, choices=[(b'medical', b'Medical'), (b'restaurants', b'Restaurants'), (b'shopping', b'Shopping'), (b'public_services', b'Public Services'), (b'transportation', b'Transportation'), (b'help', b'Help')]),
        ),
        migrations.AlterField(
            model_name='sp',
            name='desc',
            field=models.CharField(max_length=225, blank=True),
        ),
        migrations.AlterField(
            model_name='sp',
            name='discount',
            field=models.IntegerField(default=0, db_index=True, blank=True),
        ),
        migrations.AlterField(
            model_name='sp',
            name='latitude',
            field=models.DecimalField(db_index=True, max_digits=7, decimal_places=7, blank=True),
        ),
        migrations.AlterField(
            model_name='sp',
            name='longitude',
            field=models.DecimalField(db_index=True, max_digits=7, decimal_places=7, blank=True),
        ),
        migrations.AlterField(
            model_name='sp',
            name='phone',
            field=models.CharField(db_index=True, max_length=13, blank=True),
        ),
        migrations.AlterField(
            model_name='sp',
            name='website',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(db_index=True, unique=True, max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='facebook_id',
            field=models.CharField(unique=True, max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(db_index=True, max_length=35, blank=True),
        ),
    ]
