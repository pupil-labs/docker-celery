import os, json, time
from task_queue import celery_app
from flask import current_app

@celery_app.task(name='tasks.finish_transcoding_task')
def finish_transcoding_task(task_done):
    current_app.logger.info('monsterkill: '+ task_done + '....lets celebrate it ...')
    # GET the video data
    time.sleep(1)
    current_app.logger.info('enough now!')
    return "success"