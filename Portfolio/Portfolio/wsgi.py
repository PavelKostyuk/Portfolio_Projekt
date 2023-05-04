import os
from django.core.wsgi import get_wsgi_application

# Check for the PRODUCTION environment variable to see if we are running in Azure App Service
# If so, then load the settings from production.py
settings_module = 'Portfolio.production' if 'PRODUCTION' in os.environ else 'Portfolio.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)


application = get_wsgi_application()
