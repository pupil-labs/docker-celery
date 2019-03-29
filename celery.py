from __future__ import absolute_import, unicode_literals
import os, logging, sys
from api.config import config_by_name
from api import create_app
from celery import Celery

environment = os.getenv('BOILERPLATE_ENV') if os.getenv('BOILERPLATE_ENV') else 'dev'


def create_celery_app(app=None):
    """
    Create a new Celery object and tie together the Celery config to the app's
    config. Wrap all tasks in the context of the application.
    :param app: Flask app
    :return: Celery app
    """
    app = app or create_app(environment)
    
    celery = Celery(
        'task_queue',
        # app.import_name,
        backend=config_by_name[environment].CELERY_RESULT_BACKEND,
        broker=config_by_name[environment].CELERY_RESULT_BACKEND,
        include=config_by_name[environment].CELERY_TASK_LIST
    )
    # celery.conf.BROKER_USE_SSL = True
    # celery.conf.CELERY_ACCEPT_CONTENT= ['json']
    # celery.setup_security()
    celery.conf.update(app.config)

    # creates a subclass of the task that wraps the task execution in an application context.
    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

# celery_app = create_celery_app()