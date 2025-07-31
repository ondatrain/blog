"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import environ

from django.core.wsgi import get_wsgi_application

blog_control = environ.Env(
    # set casting, default value
    BLOG_SETTINGS_FILE=(str, "config.settings.dev")
)

blog_control_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

environ.Env.read_env(os.path.join(blog_control_dir, '.blog_control'))

BLOG_SETTINGS_FILE = blog_control('SETTINGS_FILE')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", BLOG_SETTINGS_FILE)

application = get_wsgi_application()
