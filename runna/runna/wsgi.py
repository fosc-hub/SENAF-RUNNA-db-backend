"""
WSGI config for runna project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
import sys
print("Python path:", sys.path)
print("DJANGO_SETTINGS_MODULE:", os.environ.get('DJANGO_SETTINGS_MODULE'))
sys.path.append('/var/task/runna')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'runna.runna.settings')

application = get_wsgi_application()

app = application