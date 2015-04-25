# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=225)),
                ('content', models.TextField()),
                ('likes', models.IntegerField(default=0, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='SP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, db_index=True)),
                ('address', models.CharField(max_length=225, db_index=True)),
                ('desc', models.CharField(max_length=225)),
                ('phone', models.CharField(max_length=13, db_index=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('discount', models.IntegerField(default=0, db_index=True)),
                ('longitude', models.DecimalField(max_digits=7, decimal_places=7, db_index=True)),
                ('latitude', models.DecimalField(max_digits=7, decimal_places=7, db_index=True)),
                ('category', models.CharField(blank=True, max_length=45, choices=[(b'medical', b'Medical'), (b'restaurants', b'Restaurants'), (b'shopping', b'Shopping'), (b'public_services', b'PublicServices'), (b'transportation', b'Transportation'), (b'help', b'Help')])),
                ('created', models.DateField(auto_now_add=True)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('facebook_id', models.CharField(unique=True, max_length=30)),
                ('first_name', models.CharField(max_length=30, db_index=True)),
                ('last_name', models.CharField(max_length=30, db_index=True)),
                ('email', models.EmailField(unique=True, max_length=254, db_index=True)),
                ('birthday', models.DateField()),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='sp',
            field=models.ForeignKey(to='togetthereApp.SP'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(to='togetthereApp.User'),
        ),
    ]
