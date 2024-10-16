import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'DJANGO_SETTINGS_MODULE' environment variable.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')  # Adjust this if your settings file is in a different module.

# Get the WSGI application.
application = get_wsgi_application()
