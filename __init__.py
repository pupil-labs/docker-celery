from celery import Celery
from api.config import config_by_name
from task_queue.celery import create_celery_app

celery_app = create_celery_app()

