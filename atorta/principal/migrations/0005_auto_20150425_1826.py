# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_auto_20150425_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido_cabecera',
            name='cliente',
            field=models.ForeignKey(default=None, blank=True, to='principal.Cliente', null=True),
        ),
    ]
