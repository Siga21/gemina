from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext

from principal.models import Articulo, Pedido_detalle, Tienda, Cliente
from principal.forms import ArticuloForm
from principal.forms import Pedido_cabeceraForm

# Create your views here.

def portada(request):
	los_articulos = Articulo.objects.all()
	context = {'los_articulos': los_articulos }
	return render(request, 'principal/index.html', context)

#--------------------------------------------------------------------	

def sobre(request):
	return render_to_response('principal/about.html')	

#--------------------------------------------------------------------	

def nuevo_articulo(request):
    if request.method=='POST':
        formulario = ArticuloForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/principal')
    else:
        formulario = ArticuloForm()
    return render_to_response('principal/articuloform.html',{'formulario':formulario}, context_instance=RequestContext(request))

#--------------------------------------------------------------------    

def buscar_articulo(request):
	return render(request, 'principal/buscar_articulo.html')    

#--------------------------------------------------------------------

def resultado_busqueda(request):
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		barticulo = Articulo.objects.filter(nombre__icontains=q)
		return render(request, 'principal/articulos_resultados.html', {'barticulo': barticulo, 'query':q})
	else:
		return render(request, 'principal/buscar_articulo.html', {'error': True})

#---------------------------------------------------------------------

def nuevo_pedido_cabecera(request):
    if request.method=='POST':
	q = request.POST['tienda'] 
	p = request.POST['cliente'] 
	#btienda = Tienda.objects.filter(id = q)	
	btienda = get_object_or_404(Tienda, pk=q)
	bcliente = get_object_or_404(Cliente, pk=p)	
	return render_to_response('principal/datos_cliente.html',{'btienda':btienda, 'bcliente':bcliente}, context_instance=RequestContext(request))
#	formulario = Pedido_cabeceraForm(request.POST, request.FILES)
#        if formulario.is_valid():
            #formulario.save()
            #return HttpResponseRedirect('/principal')
#            return render_to_response('principal/datos_cliente.html',{'formulario':formulario}, context_instance=RequestContext(request))
    else:
        formulario = Pedido_cabeceraForm()
    return render_to_response('principal/pedido_cabecera_form.html',{'formulario':formulario}, context_instance=RequestContext(request))

#--------------------------------------------------------------------


