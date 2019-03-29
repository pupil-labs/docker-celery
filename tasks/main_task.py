import os, json, time
from task_queue import celery_app
from flask import current_app

@celery_app.task(name='tasks.main_task')
def main_task(files):
    current_app.logger.info(files)
    for file in files:
        current_app.logger.info('processing awesome file ' +file['name']+' ...now lets sleep...')
        time.sleep(1)

    return  "cool: task done"

@celery_app.task(name='tasks.test')
def test_task():
	current_app.logger.info('for test only')
	return "test done"