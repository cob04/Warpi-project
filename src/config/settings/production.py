from .base import *


# Domains
# -------
ALLOWED_HOSTS = ["staging.warpi.co.ke"]

# DEBUG
# -----
DEBUG = env('DEBUG')
TEMPLATE_DEBUG = DEBUG

# SECRET CONFIGURATION
# --------------------
SECRET_KEY = env('DJANGO_SECRET_KEY')

# DATABASE CONFIGURATION
# ----------------------
DATABASES = {
	'default': env.db()
}