from django.shortcuts import render

from principal.models import Articulo

# Create your views here.

def portada(request):
	los_articulos = Articulo.objects.all()
	context = {'los_articulos': los_articulos }
	return render(request, 'principal/index.html', context)
	
