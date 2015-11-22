from HikeIt.settings import *

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hikeit_dev',
        'USER': os.environ.get("HIKEIT_DB_USER", ''),
        'PASSWORD': os.environ.get("HIKEIT_DB_PASSWORD", ''),
    }
}

STATIC_ROOT = "static"
DEBUG = True
