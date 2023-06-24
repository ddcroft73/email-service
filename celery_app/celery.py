from celery import Celery
import os


for directory in ['./broker/out', './broker/processed']:
    if not os.path.exists(directory):
        os.makedirs(directory)

app = Celery('celery_app', include=['celery_app.tasks'])

app.conf.update({
    'broker_url': 'filesystem://localhost',
    'broker_transport_options': {
        'data_folder_in': './broker/out',
        'data_folder_out': './broker/out',
        'data_folder_processed': './broker/processed'
    }
})
