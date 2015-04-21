#encoding:utf-8

from django.forms import ModelForm
from  django import forms
from principal.models import Tienda, Empleado, Articulo , Cliente , Pedido_cabecera , Pedido_detalle

class ArticuloForm(ModelForm):
	class Meta:
		model = Articulo
