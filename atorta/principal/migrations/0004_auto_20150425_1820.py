# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_auto_20150406_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='correo',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='correo',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='pedido_cabecera',
            name='tienda',
            field=models.ForeignKey(default=None, blank=True, to='principal.Tienda', null=True),
        ),
        migrations.AlterField(
            model_name='tienda',
            name='correo',
            field=models.EmailField(default=None, max_length=254, null=True, blank=True),
        ),
    ]
