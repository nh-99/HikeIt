from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from . import api

urlpatterns = [
    url(r'^(?P<query>[\w ]+)/$', views.search, name='search'),
]

apipatterns = [
    url(r'^(?P<query>[\w ]+)/$', api.Search.as_view()),
    url(r'^latlon/(?P<lat_string>-?\d+(?:\.\d+)?)/(?P<lng_string>-?\d+(?:\.\d+)?)/$', api.SearchLatLng.as_view()),
]

urlpatterns = urlpatterns + format_suffix_patterns(apipatterns)
