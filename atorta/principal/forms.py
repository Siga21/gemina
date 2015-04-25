#encoding:utf-8

from django.forms import ModelForm
from  django import forms
from principal.models import Tienda, Empleado, Articulo , Cliente , Pedido_cabecera , Pedido_detalle

class ArticuloForm(ModelForm):
	class Meta:
		model = Articulo
		fields = "__all__" 
class Pedido_cabeceraForm(ModelForm):
	class Meta:
		model = Pedido_cabecera
		fields = ('tienda', 'cliente', ) 
#class Pedido_detalleForm(forms.Form): 
#     articulo = forms.CharField() 
#     cantidad = forms.IntegerField() 
#     importe = forms.IntegerField() 

