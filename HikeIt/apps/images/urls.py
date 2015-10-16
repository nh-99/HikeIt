from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='image_index'),
    url(r'^(?P<image_id>[0-9]+)/approve/$', views.approve, name='image_approve'),
    url(r'^(?P<image_id>[0-9]+)/destroy/$', views.destroy, name='image_destroy'),
]
