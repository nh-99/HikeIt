from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^new/$', views.registeruser, name='register_new_user'),
    url(r'^approve/$', views.confirmuser, name='approve_new_user'),
]
