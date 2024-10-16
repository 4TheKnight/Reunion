import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Batchof2018.settings')

# Debugging output
print("DJANGO_SETTINGS_MODULE:", os.environ.get('DJANGO_SETTINGS_MODULE'))

try:
    application = get_wsgi_application()
except Exception as e:
    print("Error loading application:", e)
