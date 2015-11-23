# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_user_active_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForwardNews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=200, null=True, blank=True)),
                ('time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ForwardNewsComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('time', models.DateField(null=True, blank=True)),
                ('ForwardInfo', models.ForeignKey(to='mainapp.ForwardNews')),
            ],
        ),
        migrations.RemoveField(
            model_name='forwardmesg',
            name='user',
        ),
        migrations.RemoveField(
            model_name='forwardmesgcomment',
            name='ForwardInfo',
        ),
        migrations.RemoveField(
            model_name='forwardmesgcomment',
            name='user',
        ),
        migrations.AlterField(
            model_name='news',
            name='recommend_index',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='active_code',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='degree',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='icon',
            field=models.ImageField(null=True, upload_to=b'./img', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='institute',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='major',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='ForwardMesg',
        ),
        migrations.DeleteModel(
            name='ForwardMesgComment',
        ),
        migrations.AddField(
            model_name='forwardnewscomment',
            name='user',
            field=models.ForeignKey(to='mainapp.User'),
        ),
        migrations.AddField(
            model_name='forwardnews',
            name='user',
            field=models.ForeignKey(to='mainapp.User'),
        ),
    ]
