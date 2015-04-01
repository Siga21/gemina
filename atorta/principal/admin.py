from django.contrib import admin
from principal.models import Tienda, Empleado, Articulo , Cliente , Pedido_cabecera , Pedido_detalle

# Register your models here.



 
admin.site.register(Tienda) 
admin.site.register(Empleado) 
admin.site.register(Articulo) 
admin.site.register(Cliente) 
admin.site.register(Pedido_cabecera)
admin.site.register(Pedido_detalle)
