import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_with_celery.settings')

celery_app = Celery('django_with_celery')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()