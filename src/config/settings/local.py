from .base import *


########################
# DEVELOPMENT SETTINGS #
########################

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "@hxz_3)5(j)l@+kf^ub$p45zbpl4-e@izqs5_44*sts0(09^fx"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "warpi_project_db",
        "ATOMIC_REQUESTS": True,
    }
}


INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]

# Debug toolbar  middleware
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']

# Domains for public site
ALLOWED_HOSTS = ["localhost"]

EMAIL_BACKEND="django.core.mail.backends.console.EmailBackend"


