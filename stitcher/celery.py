from celery import Celery, current_app

app = Celery('celery_app', broker='redis://localhost:6379/0', backend='redis://localhost:6379/1')


@current_app.task
def start_sychronization(state):
    return {
        'image_path': 'some_path',
        **state
    }
