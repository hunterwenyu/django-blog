# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='summary',
            field=models.TextField(max_length=200, null=True, verbose_name='\u6458\u8981'),
            preserve_default=True,
        ),
    ]
