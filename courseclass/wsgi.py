"""
WSGI config for courseclass project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os

ENV = os.environ['MY_PROJECT_ENV']
if ENV == 'production':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "courseclass.settings.prod")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "courseclass.settings.local")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
