# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20151026_1035'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForwardMesg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('time', models.DateField()),
                ('user', models.ForeignKey(to='mainapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='ForwardMesgComments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('time', models.DateField()),
                ('ForwardInfo', models.ForeignKey(to='mainapp.ForwardMesg')),
                ('user', models.ForeignKey(to='mainapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='ReleaseMesg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('time', models.DateField()),
                ('user', models.ForeignKey(to='mainapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='ReleaseMesgComments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('time', models.DateField()),
                ('ReleaseInfo', models.ForeignKey(to='mainapp.ReleaseMesg')),
                ('user', models.ForeignKey(to='mainapp.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='userforwardmesg',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userforwardmesgcomments',
            name='ForwardInfo',
        ),
        migrations.RemoveField(
            model_name='userforwardmesgcomments',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userreleasemesg',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userreleasemesgcomments',
            name='ReleaseInfo',
        ),
        migrations.RemoveField(
            model_name='userreleasemesgcomments',
            name='user',
        ),
        migrations.RenameField(
            model_name='interesttribe',
            old_name='theam',
            new_name='theme',
        ),
        migrations.DeleteModel(
            name='UserForwardMesg',
        ),
        migrations.DeleteModel(
            name='UserForwardMesgComments',
        ),
        migrations.DeleteModel(
            name='UserReleaseMesg',
        ),
        migrations.DeleteModel(
            name='UserReleaseMesgComments',
        ),
    ]
