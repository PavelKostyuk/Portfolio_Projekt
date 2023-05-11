import os
import sys
from django.core.wsgi import get_wsgi_application

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, 'Portfolio'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Portfolio.settings')

application = get_wsgi_application()