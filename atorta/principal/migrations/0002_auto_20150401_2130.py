# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('familia', models.CharField(max_length=50)),
                ('importe', models.IntegerField()),
                ('antiguedad', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('fotografia', models.ImageField(upload_to=b'imagenes')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=50)),
                ('poblacion', models.CharField(max_length=60)),
                ('provincia', models.CharField(max_length=20)),
                ('pais', models.CharField(max_length=20)),
                ('telefono', models.PositiveIntegerField(null=True, blank=True)),
                ('correo', models.EmailField(max_length=75)),
                ('pedidos', models.CharField(max_length=10)),
                ('importe', models.IntegerField()),
                ('antiguedad', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('ultimo_pedido', models.DateTimeField(default=datetime.datetime.now, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pedido_cabecera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tienda', models.CharField(max_length=10)),
                ('cliente', models.CharField(max_length=10)),
                ('cantidad', models.CharField(max_length=100)),
                ('importe', models.IntegerField()),
                ('fecha', models.DateTimeField(default=datetime.datetime.now, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pedido_detalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField(max_length=100)),
                ('importe', models.IntegerField()),
                ('articulo', models.ManyToManyField(to='principal.Articulo')),
                ('pedido', models.ManyToManyField(to='principal.Pedido_cabecera')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
        migrations.RenameField(
            model_name='empleado',
            old_name='email',
            new_name='correo',
        ),
        migrations.RenameField(
            model_name='tienda',
            old_name='domicilio',
            new_name='direccion',
        ),
        migrations.RemoveField(
            model_name='tienda',
            name='ciudad',
        ),
        migrations.RemoveField(
            model_name='tienda',
            name='estado',
        ),
        migrations.AddField(
            model_name='empleado',
            name='antiguedad',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='empleado',
            name='direccion',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='empleado',
            name='pais',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='empleado',
            name='poblacion',
            field=models.CharField(max_length=60, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='empleado',
            name='provincia',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='empleado',
            name='telefono',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='empleado',
            name='tienda',
            field=models.ForeignKey(default=None, blank=True, to='principal.Tienda', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tienda',
            name='antiguedad',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tienda',
            name='correo',
            field=models.EmailField(default=None, max_length=75, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tienda',
            name='fax',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tienda',
            name='poblacion',
            field=models.CharField(default=None, max_length=60, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tienda',
            name='provincia',
            field=models.CharField(default=None, max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tienda',
            name='telefono',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tienda',
            name='pais',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
    ]
