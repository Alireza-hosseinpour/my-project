# SECURITY WARNING: keep the secret key used in production secret!
from my_project.settings import *


SECRET_KEY = 'django-insecure-t++o&a_986!9kgo!v#k0*_b+6%5sk4pfr^u)3c+0dbhg!8pc5b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

#INSTALLED_APPS = []



#sites framework
SITE_ID = 2

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT =BASE_DIR/'static'
MEDIA_ROOT =BASE_DIR/'media'

STATICFILES_DIRS=[
    BASE_DIR/'assets',
      ]


#CSRF_COOKIE_SECURE = True