from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from . import api

urlpatterns = [
    url(r'^(?P<trail_id>[0-9]+)/$', views.trailpage, name='trail'),
    url(r'^(?P<trail_id>[0-9]+)/like$', views.liketrail, name='liketrail'),
    url(r'^(?P<trail_id>[0-9]+)/completed$', views.completedtrail, name='completedtrail'),
    url(r'^(?P<trail_id>[0-9]+)/save$', views.savedtrail, name='savedtrail'),
    url(r'^(?P<trail_id>[0-9]+)/upload/', views.upload_trail_image, name='trail_image_upload'),
    url(r'^(?P<trail_id>[0-9]+)/review/', views.create_review, name='create_review'),
    url(r'^(?P<trail_id>[0-9]+)/location/', views.traillocation, name='trail_location'),
    url(r'^new/$', views.new, name='newtrail'),
    url(r'^create/$', views.create_trail, name='createtrail'),
    url(r'^trails/$', views.approve_trail_list, name='approve_trail_list'),
    url(r'^approve/$', views.approve_trail, name='approve_trail'),
]

apipatterns = [
    url(r'^(?P<pk>[0-9]+)/$', api.TrailInfo.as_view()),
]

urlpatterns = urlpatterns + format_suffix_patterns(apipatterns)
