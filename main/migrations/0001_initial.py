# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('slug', models.SlugField(verbose_name='\u0421\u043b\u0443\u0436\u0435\u0431\u043d\u043e\u0435 \u043f\u043e\u043b\u0435')),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
            ],
        ),
    ]
