from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<trail_id>[0-9]+)/$', views.planner, name='hike_planner'),
    url(r'^plan/$', views.plan, name='plan'),
]
