##################
# LOCAL SETTINGS #
##################

from .base import *


# Domains
# -------
ALLOWED_HOSTS = ["localhost"]

# DEBUG
# -----
DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# SECRET CONFIGURATION
# --------------------
SECRET_KEY = env('DJANGO_SECRET_KEY', default="@hxz_3)5(j)l@+kf^ub$p45zbpl4-e@izqs5_44*sts0(09^fx")

# Mail settings
# -------------
EMAIL_BACKEND="django.core.mail.backends.console.EmailBackend"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "warpi_project_db",
        "ATOMIC_REQUESTS": True,
    }
}


# django-debug-toolbar
# --------------------
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]

INSTALLED_APPS += ['debug_toolbar',]

INTERNAL_IPS = ['127.0.0.1']

# django-extensions
# -----------------
INSTALLED_APPS += ['django_extensions',]
