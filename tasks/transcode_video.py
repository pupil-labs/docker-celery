import os, json, time
from task_queue import celery_app
from flask import current_app


@celery_app.task(name='tasks.transcode_video')
def transcode_video(video_data):
    current_app.logger.info('cool we got video data from video: {} ....lets transcode it...'.format(str(video_data)))
    # GET the video data
    time.sleep(1)
    current_app.logger.info('transcoding done!')
    return "transcoded data from video: "+ video_data