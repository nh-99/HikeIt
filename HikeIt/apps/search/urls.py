from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from . import api

urlpatterns = [
    url(r'^location/(?P<location>[\w ]+)/$', views.location, name='location'),
    url(r'^name/(?P<name>[\w ]+)/$', views.name, name='name'),
]

apipatterns = [
    url(r'^location/(?P<location>[\w ]+)/$', api.SearchLocation.as_view()),
    url(r'^name/(?P<name>[\w ]+)/$', api.SearchName.as_view()),
]

urlpatterns = urlpatterns + format_suffix_patterns(apipatterns)
