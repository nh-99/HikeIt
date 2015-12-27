from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<trail_id>[0-9]+)/$', views.planner, name='hike_planner'),
    url(r'^(?P<planner_id>[0-9]+)/view/$', views.view_plan, name='view_plan'),
    url(r'^(?P<planner_id>[0-9]+)/delete/$', views.delete_plan, name='delete_plan'),
    url(r'^plan/$', views.plan, name='plan'),
]
