from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^new/$', views.registeruser, name='register_new_user'),
    url(r'^approve/$', views.confirmuser, name='approve_new_user'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/settings/$', views.profile_settings, name='profile_settings'),
    url(r'^edit/$', views.update_profile, name='update_profile'),
]

from rest_framework.authtoken import views
urlpatterns += [
    url(r'^token/', views.obtain_auth_token)
]
