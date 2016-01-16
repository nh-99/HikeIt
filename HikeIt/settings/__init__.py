"""
Django settings for HikeIt project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import djcelery
from django.contrib.messages import constants as messages
from .config import *

djcelery.setup_loader()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('HIKEIT_SECRET_KEY', 'jaksdjfkasjdfkljJoi2uroijlkF98234ijknkjajkl')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# Application definition

INSTALLED_APPS = (
    'bootstrap_admin',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'django_jenkins',
    'widget_tweaks',
    'password_reset',
    'trails',
    'paths',
    'reviews',
    'issues',
    'search',
    'static_pages',
    'images',
    'users',
    'planner',
    'django.contrib.auth',
    'rest_framework',
    'rest_framework.authtoken',
    'djcelery'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'HikeIt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

HOSTNAME = os.environ.get('HIKEIT_HOSTNAME')

WSGI_APPLICATION = 'HikeIt.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT = 'media'
MEDIA_URL = '/images/'

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', 
    'social.backends.facebook.FacebookOAuth2',
)

ACCOUNT_ACTIVATION_DAYS = 7

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_URL = '/login'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
AUTH_PROFILE_MODULE = 'users.UserTrails'
LOGIN_REDIRECT_URL = '/'

EMAIL_USE_SSL = True
EMAIL_HOST = 'hikeit.me'
EMAIL_PORT = 465
EMAIL_HOST_USER = os.environ.get('HIKEIT_EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('HIKEIT_EMAIL_PASS')

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '2000/day',
        'user': '5000/day'
    },
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}

BROKER_URL = 'amqp://guest:guest@localhost:5672/'
BOOTSTRAP_ADMIN_SIDEBAR_MENU = True
