from celery import shared_task


@shared_task(bind=True)
def test_func(self):
    print('Hello world')
    return 'Done'