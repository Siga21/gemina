from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^principal/', 'principal.views.portada', name = 'portada'),
    url(r'^sobre/', 'principal.views.sobre', name = 'sobre'),
)
