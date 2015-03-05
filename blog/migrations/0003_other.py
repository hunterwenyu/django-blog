# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=10, verbose_name='\u535a\u4e3b\u7f51\u540d')),
                ('motto', models.CharField(max_length=20, verbose_name='\u5934\u50cf\u4e0b\u65b9\u7b7e\u540d')),
                ('salutatory', models.CharField(max_length=200, null=True, verbose_name='\u9996\u9875\u6b22\u8fce\u8bcd')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
