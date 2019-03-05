from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^shows/new$', views.new),
    url(r'^shows/create$', views.create),
    url(r'^shows$', views.readA),
    url(r'^shows/(?P<num>\d+)/edit$', views.edit),
    url(r'^shows/(?P<num>\d+)/update$', views.update),
    url(r'^shows/(?P<num>\d+)$', views.readO),
    url(r'^shows/(?P<num>\d+)/destroy$', views.delete),
]