from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from . import api

urlpatterns = [
    url(r'^new/$', views.registeruser, name='register_new_user'),
    url(r'^approve/$', views.confirmuser, name='approve_new_user'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/trails/$', views.profile_trails, name='profile_trails'),
    url(r'^profile/settings/$', views.profile_settings, name='profile_settings'),
    url(r'^edit/$', views.update_profile, name='update_profile'),
]

# Token auth
from rest_framework.authtoken import views
urlpatterns += [
    url(r'^token/', views.obtain_auth_token),
]

apipatterns = [
    url(r'^profile/$', api.UserInfo.as_view()),
    url(r'^register/$', api.Register.as_view()),
]

urlpatterns = urlpatterns + format_suffix_patterns(apipatterns)
