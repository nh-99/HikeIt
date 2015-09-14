from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^delete/(?P<review_id>[0-9]+)/$', views.delete_review, name='review_delete'),
]
