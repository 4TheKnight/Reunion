import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'django' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')  # No need for Batchof2018 prefix since you are in the same directory.

# Get the WSGI application.
application = get_wsgi_application()
