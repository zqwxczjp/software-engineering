# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20151026_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserForwardMesg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('time', models.DateField()),
                ('user', models.ForeignKey(to='mainapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserForwardMesgComments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('time', models.DateField()),
                ('ForwardInfo', models.ForeignKey(to='mainapp.UserForwardMesg')),
                ('user', models.ForeignKey(to='mainapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserReleaseMesg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('time', models.DateField()),
                ('comments', models.TextField()),
                ('user', models.ForeignKey(to='mainapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserReleaseMesgComments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('time', models.DateField()),
                ('ReleaseInfo', models.ForeignKey(to='mainapp.UserReleaseMesg')),
                ('user', models.ForeignKey(to='mainapp.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='userforwardinfo',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userforwardinfocomments',
            name='ForwardInfo',
        ),
        migrations.RemoveField(
            model_name='userforwardinfocomments',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userreleaseinfo',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userreleaseinfocomments',
            name='ReleaseInfo',
        ),
        migrations.RemoveField(
            model_name='userreleaseinfocomments',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserForwardInfo',
        ),
        migrations.DeleteModel(
            name='UserForwardInfoComments',
        ),
        migrations.DeleteModel(
            name='UserReleaseInfo',
        ),
        migrations.DeleteModel(
            name='UserReleaseInfoComments',
        ),
    ]
