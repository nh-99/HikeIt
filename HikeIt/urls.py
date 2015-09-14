"""HikeIt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),
    url(r'^$', include('static_pages.urls')),
    url(r'^planner/', include('planner.urls')),
    url(r'^trail/', include('trails.urls')),
    url(r'^image/', include('images.urls')),
    url(r'^paths/', include('paths.urls')),
    url(r'^reviews/', include('reviews.urls')),
    url(r'^user/', include('users.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^password/', include('password_reset.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    
    # Auth
    url('^', include('django.contrib.auth.urls'), {'template_name': 'users/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
