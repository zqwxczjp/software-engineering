# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_auto_20151221_2306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.TextField()),
                ('Url', models.URLField()),
                ('Teacher', models.TextField()),
                ('School', models.TextField()),
            ],
        ),
    ]
