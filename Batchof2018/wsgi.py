import os
from pathlib import Path
from django.core.wsgi import get_wsgi_application

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Batchof2018.settings')

# Add the project path to the Python path
project_path = Path(__file__).resolve().parent.parent
if project_path not in os.sys.path:
    os.sys.path.append(str(project_path))

application = get_wsgi_application()
