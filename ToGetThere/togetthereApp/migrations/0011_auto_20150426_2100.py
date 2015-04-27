# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('togetthereApp', '0010_auto_20150426_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, db_index=True)),
                ('city', models.ForeignKey(to='togetthereApp.City')),
            ],
        ),
        migrations.RemoveField(
            model_name='sp',
            name='address',
        ),
        migrations.AddField(
            model_name='sp',
            name='street_num',
            field=models.IntegerField(default=1, db_index=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sp',
            name='city',
            field=models.ForeignKey(to='togetthereApp.City'),
        ),
        migrations.AddField(
            model_name='sp',
            name='street',
            field=models.ForeignKey(default='street', to='togetthereApp.Street'),
            preserve_default=False,
        ),
    ]
