# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_newscomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forwardnews',
            name='time',
            field=models.TextField(null=True),
        ),
    ]
