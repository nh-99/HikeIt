from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='reviews_index'),
    url(r'^approve/(?P<review_id>[0-9]+)/$', views.approve, name='review_approve'),
]
