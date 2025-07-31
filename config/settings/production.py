from .base import *
import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

if os.environ.get('REMOTE_HOSTED_BLOG') is None:
    # Take environment variables from .env file
    environ.Env.read_env(os.path.join(BASE_DIR, '.env.prod'))

# False if not in os.environ because of casting above
DEBUG = env('DEBUG')

# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

db_params = {
    'default': env.db(),
}

# Secure connection using a public certificate
CERT_DIR = env('CERT_DIR')
SSL_ROOT_CERT = os.path.join(BASE_DIR, CERT_DIR)

db_params['default'].update({
    'OPTIONS': {
        'sslmode': 'verify-ca',
        'sslrootcert': SSL_ROOT_CERT
    }
})

DATABASES = db_params

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', cast=str)

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

if env.bool('REMOTE_HOSTED_BLOG', default=False) and env.bool('LOG_ENABLED', default=False):
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '{levelname} {asctime} {module} {message}',
                'style': '{',
            },
            'simple': {
                'format': '{levelname} {message}',
                'style': '{',
            },
        },
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': 'debug.log',
                'formatter': 'verbose',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': env('LOG_CONSOLE_LEVEL'),
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': True,
            },
        },
    }


try:
    from .local import *
except ImportError:
    pass
