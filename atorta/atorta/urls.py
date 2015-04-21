from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = patterns('',
	url(r'^imagenes/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^principal/', 'principal.views.portada', name = 'portada'),
    url(r'^articulo/nuevo/$' , 'principal.views.nuevo_articulo'),
    url(r'^sobre/', 'principal.views.sobre', name = 'sobre'),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

