# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20151123_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='ReqDirection',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='forwardnews',
            name='time',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='forwardnews',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
