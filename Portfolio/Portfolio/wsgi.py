import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, 'Portfolio'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Portfolio.settings')
