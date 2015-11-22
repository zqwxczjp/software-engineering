# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20151026_1053'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForwardMesgComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('time', models.DateField()),
                ('ForwardInfo', models.ForeignKey(to='mainapp.ForwardMesg')),
                ('user', models.ForeignKey(to='mainapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='ReleaseMesgComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('time', models.DateField()),
                ('ReleaseInfo', models.ForeignKey(to='mainapp.ReleaseMesg')),
                ('user', models.ForeignKey(to='mainapp.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='forwardmesgcomments',
            name='ForwardInfo',
        ),
        migrations.RemoveField(
            model_name='forwardmesgcomments',
            name='user',
        ),
        migrations.RemoveField(
            model_name='releasemesgcomments',
            name='ReleaseInfo',
        ),
        migrations.RemoveField(
            model_name='releasemesgcomments',
            name='user',
        ),
        migrations.DeleteModel(
            name='ForwardMesgComments',
        ),
        migrations.DeleteModel(
            name='ReleaseMesgComments',
        ),
    ]
