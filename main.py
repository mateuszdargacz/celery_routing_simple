from celery import Celery, signature

app = Celery('celery_app', broker='redis://localhost:6379/0', backend='redis://localhost:6379/1')


# generally that's how routing will be defined in simple example
app.conf.task_routes = {
    'stitcher.celery.*': {'queue': 'stitcher'},
    'backend.celery.*': {'queue': 'backend'}
}

app.conf.task_default_queue = 'backend'


if __name__ == "__main__":
    initial_state = dict(state=dict(something='somethingelse'))
    # define task signatures
    start_sychronization_s = signature('stitcher.celery.start_sychronization', kwargs=initial_state, queue='stitcher')
    save_to_database = signature('backend.celery.save_to_database', queue='backend')
    # chain tasks a'la  callback
    chain = start_sychronization_s | save_to_database
    res = chain.apply_async()
    print('Result', res.get())
