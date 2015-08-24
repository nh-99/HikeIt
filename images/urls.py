from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='image_index'),
    url(r'^approve/(?P<image_id>[0-9]+)/$', views.approve, name='image_approve'),
]
