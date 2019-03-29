import os, json, time, boto3
from task_queue import celery_app
from flask import current_app

@celery_app.task(name='tasks.get_video_data')
def get_video_data(file):
    s3 = S3Service()
    mode = 'wb'
    current_app.logger.info('here!!')
    current_app.logger.info(file['file_key'])
    #with open('test', mode) as data:
    #    dat = s3.client.download_fileobj(Bucket='pupil-cloud-staging',Key=file['file_key'],Fileobj=data)
    #    current_app.logger.info(data)

    obj = s3.client.get_object(Bucket='pupil-cloud-staging', Key=file['file_key'])
    current_app.logger.info(obj)
    return 'test'



def createS3Instance(file):
    s3 = S3Service()

    client = s3.client

class S3Service:

    def __init__(self):
        # Create an S3 client

        self.client = boto3.client('s3',
                      region_name=os.getenv('spaces_region'),
                      endpoint_url='https://{}.digitaloceanspaces.com'.format(os.getenv('spaces_region')),
                      aws_access_key_id=os.getenv('spaces_access_key'),
                      aws_secret_access_key=os.getenv('spaces_secret_key'))