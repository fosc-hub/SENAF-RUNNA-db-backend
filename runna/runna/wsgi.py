"""
WSGI config for runna project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

# Add the project root to the Python path
sys.path.append('/var/task/runna')  # Adjust this if your deployment root is different

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'runna.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
app = application
