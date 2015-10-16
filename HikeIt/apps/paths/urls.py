from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<trail_id>[0-9]+)/upload/', views.upload_trail_path, name='path_upload'),
]
