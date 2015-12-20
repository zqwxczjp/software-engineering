# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20151219_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendMesg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userFrom', models.IntegerField()),
                ('userTo', models.IntegerField()),
                ('Content', models.TextField()),
                ('Time', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
