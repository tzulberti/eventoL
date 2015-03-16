# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sede',
            name='url',
            field=models.CharField(default='old', help_text='URL for the sede i.e. CABA', max_length=200, verbose_name='URL'),
            preserve_default=False,
        ),
    ]