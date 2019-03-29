FROM python:3.7.1

# ENV LANG en_US.utf8

RUN mkdir -p /root/task_queue

ADD . /root/task_queue

WORKDIR /root/task_queue

RUN apt-get update && \
	pip install --upgrade pip

RUN apt-get install -y sudo

# RUN apt-get install rabbitmq-server -y

RUN pip install --upgrade --no-cache-dir -r requirements.txt

ENV CELERY_VERSION 4.3.0rc1

RUN pip install celery=="$CELERY_VERSION"