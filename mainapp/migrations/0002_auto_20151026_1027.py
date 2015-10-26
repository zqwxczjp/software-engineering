# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserForwardInfoComments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='UserReleaseInfoComments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('time', models.DateField()),
                ('ReleaseInfo', models.ForeignKey(to='mainapp.UserReleaseInfo')),
                ('user', models.ForeignKey(to='mainapp.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='userforwardinfo',
            name='comments',
        ),
        migrations.AddField(
            model_name='userforwardinfocomments',
            name='ForwardInfo',
            field=models.ForeignKey(to='mainapp.UserForwardInfo'),
        ),
        migrations.AddField(
            model_name='userforwardinfocomments',
            name='user',
            field=models.ForeignKey(to='mainapp.User'),
        ),
    ]
