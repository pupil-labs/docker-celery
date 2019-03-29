import os, json, time
from task_queue import celery_app
from flask import current_app


@celery_app.task(name='tasks.merge_videos')
def merge_videos(transcoded_videos):
    current_app.logger.info('wow we got the follwong transcoded stuff: ')
    for files in transcoded_videos:
        current_app.logger.info(files + ' ')

    current_app.logger.info('...now merge it...')
    # GET the video data
    time.sleep(1)
    current_app.logger.info('merging done!')
    return "merged video data"