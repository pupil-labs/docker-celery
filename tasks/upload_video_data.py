import os, json, time
from task_queue import celery_app
from flask import current_app

@celery_app.task(name='tasks.upload_videos')
def upload_videos(merged_video):
    current_app.logger.info('awesome this is transcoded and merged: {} ....lets upload it ...'.format(str(merged_video)) )
    # GET the video data
    time.sleep(1)
    current_app.logger.info('uploading done!')
    return "add taks done"
