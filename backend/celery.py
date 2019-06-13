from celery import Celery, current_app

app = Celery('celery_app', broker='redis://localhost:6379/0', backend='redis://localhost:6379/1')


@current_app.task
def save_to_database(state):
    print('START', state)
    return f'{state} has ben saved to db'
