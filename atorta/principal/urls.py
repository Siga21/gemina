from django.conf.urls import url

from principal import views

urlpatterns = [
	url(r'^$', views.portada, name='portada'),
	url(r'^sobre/$', views.sobre, name='sobre'),
]
