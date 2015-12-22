# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Picurl',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
