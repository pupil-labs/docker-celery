import os, json, time
from task_queue import celery_app
from flask import current_app
from celery import chord, chain

from task_queue.tasks.finish_transcoding_task import finish_transcoding_task
from task_queue.tasks.get_video_data import get_video_data
from task_queue.tasks.merge_videos import merge_videos
from task_queue.tasks.transcode_video import transcode_video
from task_queue.tasks.upload_video_data import upload_videos


def create_transcoding_workflow(files):
    current_app.logger.info("start creating workflow...")
    transcode_and_combine = create_transcode_and_combine_chord(files)
    transcoding_workflow = chain(transcode_and_combine,upload_videos.s(),finish_transcoding_task.s())
    current_app.logger.info("workflow created!")
    return transcoding_workflow    #.set(queue=PRIORITY_QUEUE)


def create_transcode_and_combine_chord(files):
    chained_tasks = []
    current_app.logger.info("adding files to workflow...")
    for file in files:
        chained_tasks.append(chain(get_video_data.s(file),transcode_video.s()))
        current_app.logger.info("appended "+  file['name'] + " to file list")
    main_chord = chord(chained_tasks,body=merge_videos.s())
    current_app.logger.info("chord created")
    return main_chord
