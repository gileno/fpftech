from celery import shared_task


@shared_task
def task_print():
    print('Oi Celery')


@shared_task
def period_task_print():
    print("Teste")
