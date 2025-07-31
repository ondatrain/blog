from .base import *
import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env.dev'))

# False if not in os.environ because of casting above
DEBUG = env('DEBUG')

# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

# Parse DATABASE_URL connection url strings
DATABASES = {
    # ImproperlyConfigured exception if DATABASE_URL not found
    #
    # The db() method is an alias for db_url().
    'default': env.db(),
}

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', cast=str)

# Habilita django-extensions en desarrollo
INSTALLED_APPS.append('django_extensions')

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass