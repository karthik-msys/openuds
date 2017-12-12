# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-05 04:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uds', '0020_auto_20160216_0509'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarAccess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(default=None, max_length=50, null=True, unique=True)),
                ('access', models.CharField(default='DENY', max_length=8)),
                ('priority', models.IntegerField(db_index=True, default=0)),
                ('calendar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uds.Calendar')),
            ],
            options={
                'ordering': ('priority',),
                'db_table': 'uds_cal_access',
            },
        ),
        migrations.CreateModel(
            name='CalendarAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(default=None, max_length=50, null=True, unique=True)),
                ('action', models.CharField(default='', max_length=64)),
                ('at_start', models.BooleanField(default=False)),
                ('events_offset', models.IntegerField(default=0)),
                ('params', models.CharField(default='', max_length=1024)),
                ('last_execution', models.DateTimeField(blank=True, db_index=True, default=None, null=True)),
                ('next_execution', models.DateTimeField(blank=True, db_index=True, default=None, null=True)),
                ('calendar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uds.Calendar')),
            ],
            options={
                'db_table': 'uds_cal_action',
            },
        ),
        migrations.CreateModel(
            name='DBFile',
            fields=[
                ('uuid', models.CharField(default=None, max_length=50, null=True, unique=True)),
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('content', models.TextField(blank=True)),
                ('size', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='deployedservice',
            name='fallbackAccess',
            field=models.CharField(default='ALLOW', max_length=8),
        ),
        migrations.AddField(
            model_name='calendaraction',
            name='service_pool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uds.DeployedService'),
        ),
        migrations.AddField(
            model_name='calendaraccess',
            name='service_pool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uds.DeployedService'),
        ),
        migrations.AddField(
            model_name='deployedservice',
            name='accessCalendars',
            field=models.ManyToManyField(related_name='accessSP', through='uds.CalendarAccess', to='uds.Calendar'),
        ),
        migrations.AddField(
            model_name='deployedservice',
            name='actionsCalendars',
            field=models.ManyToManyField(related_name='actionsSP', through='uds.CalendarAction', to='uds.Calendar'),
        ),
    ]
