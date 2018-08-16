"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys
path = os.path.abspath(os.path.join(os.getcwd(),".."))
if path not in sys.path:
    sys.path.append(path)

from django.contrib.staticfiles.handlers import StaticFilesHandler
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
application = StaticFilesHandler(get_wsgi_application())
#application = get_wsgi_application()
