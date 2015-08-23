from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.loginpage, name='login'),
    url(r'^logout/$', views.logout_user, name='logout_user'),
]
