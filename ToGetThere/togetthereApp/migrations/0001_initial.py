# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
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
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=225)),
                ('content', models.TextField(blank=True)),
                ('likes', models.IntegerField(default=0, db_index=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, db_index=True)),
                ('desc', models.CharField(max_length=225, blank=True)),
                ('street_num', models.IntegerField(db_index=True)),
                ('longitude', models.DecimalField(db_index=True, null=True, max_digits=7, decimal_places=7, blank=True)),
                ('latitude', models.DecimalField(db_index=True, null=True, max_digits=7, decimal_places=7, blank=True)),
                ('phone', models.CharField(db_index=True, max_length=13, blank=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('discount', models.IntegerField(default=0, db_index=True, blank=True)),
                ('category', models.CharField(max_length=45, choices=[(b'medical', b'Medical'), (b'restaurants', b'Restaurants'), (b'shopping', b'Shopping'), (b'public_services', b'Public Services'), (b'transportation', b'Transportation'), (b'help', b'Help')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('website', models.URLField(blank=True)),
                ('rank', models.BigIntegerField(default=0, blank=True)),
                ('voters', models.IntegerField(default=0, blank=True)),
                ('city', models.ForeignKey(to='togetthereApp.City')),
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
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('facebook_id', models.CharField(unique=True, max_length=30, blank=True)),
                ('first_name', models.CharField(max_length=35, db_index=True)),
                ('last_name', models.CharField(db_index=True, max_length=35, blank=True)),
                ('email', models.EmailField(db_index=True, unique=True, max_length=254, blank=True)),
                ('birthday', models.DateField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='sp',
            name='street',
            field=models.ForeignKey(to='togetthereApp.Street'),
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
        migrations.AlterUniqueTogether(
            name='sp',
            unique_together=set([('name', 'street', 'street_num')]),
        ),
    ]
