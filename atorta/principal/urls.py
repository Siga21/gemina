from django.conf.urls import url

from principal import views

urlpatterns = [
	url(r'^$', views.portada, name='portada'),
]
