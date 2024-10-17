import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Main.settings')

application = get_wsgi_application()
