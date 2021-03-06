from django.db import models
from datetime import datetime

# Create your models here.

class Tienda(models.Model): 
    nombre = models.CharField(max_length=30) 
    direccion = models.CharField(max_length=50) 
    poblacion = models.CharField(max_length=60,default=None, null=True, blank=True) 
    provincia = models.CharField(max_length=20,default=None, null=True, blank=True) 
    pais = models.CharField(max_length=20) 
    telefono =  models.PositiveIntegerField(null=True, blank=True)
    fax = models.PositiveIntegerField(null=True, blank=True) 
    correo = models.EmailField(default=None, null=True, blank=True)
    website = models.URLField() 
    antiguedad = models.DateTimeField(default=datetime.now, blank=True)
    
    def __unicode__(self):
    	return self.nombre
 
 
class Empleado(models.Model): 
    nombre = models.CharField(max_length=30) 
    apellidos = models.CharField(max_length=40) 
    direccion = models.CharField(max_length=50, null=True) 
    poblacion = models.CharField(max_length=60, null=True) 
    provincia = models.CharField(max_length=20, null=True) 
    pais = models.CharField(max_length=20, null=True) 
    telefono = models.PositiveIntegerField(null=True, blank=True)
    correo = models.EmailField() 
    tienda = models.ForeignKey(Tienda, default=None, null=True, blank=True)
    antiguedad = models.DateTimeField(default=datetime.now, blank=True)
    
    def __unicode__(self):
    	return self.nombre
 

class Articulo(models.Model): 
    nombre = models.CharField(max_length=50) 
    familia = models.CharField(max_length=50)
    importe = models.DecimalField(max_digits=10, decimal_places=2) 
    antiguedad = models.DateTimeField(default=datetime.now, blank=True)
    fotografia = models.ImageField(upload_to='imagenes')
    
    def __unicode__(self):
    	return self.nombre
 
    
class Cliente(models.Model): 
    nombre = models.CharField(max_length=30) 
    apellidos = models.CharField(max_length=40) 
    direccion = models.CharField(max_length=50) 
    poblacion = models.CharField(max_length=60) 
    provincia = models.CharField(max_length=20) 
    pais = models.CharField(max_length=20) 
    telefono = models.PositiveIntegerField(null=True, blank=True)
    correo = models.EmailField() 
    pedidos = models.CharField(max_length=10)
    importe = models.IntegerField()
    antiguedad = models.DateTimeField(default=datetime.now, blank=True)
    ultimo_pedido = models.DateTimeField(default=datetime.now, blank=True)
    
    def __unicode__(self):
    	return self.nombre
 

class Pedido_cabecera(models.Model): 
    tienda = models.ForeignKey(Tienda, default=None, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, default=None, null=True, blank=True)
    cantidad = models.CharField(max_length=100) 
    importe = models.IntegerField()
    fecha = models.DateTimeField(default=datetime.now, blank=True)

class Pedido_detalle(models.Model): 
    pedido = models.ManyToManyField(Pedido_cabecera) 
    articulo = models.ManyToManyField(Articulo)
    cantidad = models.IntegerField(max_length=100) 
    importe = models.IntegerField()
    
