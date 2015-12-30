from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.index),
    url(r"^tos/$", views.tos),
    url(r"^privacy/$", views.privacy),
    url(r"^pebble/configure/$", views.pebble_config),
    url(r"^pebble/facebook/login/$", views.pebble_facebook_login),
]
