from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<trail_id>[0-9]+)/$', views.trailpage, name='trail'),
    url(r'^(?P<trail_id>[0-9]+)/like$', views.liketrail, name='liketrail'),
    url(r'^(?P<trail_id>[0-9]+)/completed$', views.completedtrail, name='completedtrail'),
    url(r'^(?P<trail_id>[0-9]+)/upload/', views.upload_trail_image, name='trail_image_upload'),
    url(r'^(?P<trail_id>[0-9]+)/review/', views.create_review, name='create_review'),
    url(r'^(?P<trail_id>[0-9]+)/location/', views.traillocation, name='trail_location'),
]
