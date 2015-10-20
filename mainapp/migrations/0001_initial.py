# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userID', models.IntegerField()),
                ('friendID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='InterestTribe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ThreadID', models.IntegerField()),
                ('theam', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source_url', models.URLField()),
                ('title', models.TextField()),
                ('author', models.TextField()),
                ('content', models.TextField()),
                ('time', models.TextField()),
                ('recommend_index', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('institute', models.CharField(max_length=50)),
                ('major', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('icon', models.ImageField(upload_to=b'./img')),
                ('degree', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserForwardInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('time', models.DateField()),
                ('comments', models.TextField()),
                ('user', models.ForeignKey(to='mainapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserReleaseInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('time', models.DateField()),
                ('comments', models.TextField()),
                ('user', models.ForeignKey(to='mainapp.User')),
            ],
        ),
        migrations.AddField(
            model_name='interesttribe',
            name='user',
            field=models.ForeignKey(to='mainapp.User'),
        ),
    ]
