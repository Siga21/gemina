from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext

from principal.models import Articulo
from principal.forms import ArticuloForm

# Create your views here.

def portada(request):
	los_articulos = Articulo.objects.all()
	context = {'los_articulos': los_articulos }
	return render(request, 'principal/index.html', context)
	
def sobre(request):
	return render_to_response('principal/about.html')	
	

def nuevo_articulo(request):
    if request.method=='POST':
        formulario = ArticuloForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/principal')
    else:
        formulario = ArticuloForm()
    return render_to_response('principal/articuloform.html',{'formulario':formulario}, context_instance=RequestContext(request))
    
def buscar_articulo(request):
	return render(request, 'principal/buscar_articulo.html')    

def resultado_busqueda(request):
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		barticulo = Articulo.objects.filter(nombre__icontains=q)
		return render(request, 'principal/articulos_resultados.html', {'barticulo': barticulo, 'query':q})
	else:
		return render(request, 'principal/buscar_articulo.html', {'error': True})
