from celery import Celery

app = Celery('celery_app',
             broker='amqp://gendis:225373@localhost/gendis_vhost',
             backend='rpc://',
             include=['celery_app.tasks'])
