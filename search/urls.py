from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^location/(?P<location>[\w ]+)/$', views.location, name='location'),
    url(r'^name/(?P<name>[\w ]+)/$', views.name, name='name'),
]
