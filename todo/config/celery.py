import os
from datetime import timedelta

from celery import Celery
from django.core.mail import send_mail
from django.utils import timezone


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# set the default Django settings module for the 'celery' program.

app = Celery('config')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')


import django
django.setup()


# Load task modules from all registered Django app configs.
app.autodiscover_tasks(force=True)


from todo.models import Todo


@app.task(name='send_notification_mail')
def send_notification_mail():
    todos = Todo.objects.all().exclude(is_done=True).exclude(expiration=None)
    now = timezone.localtime()
    zero = timedelta(0)
    an_hour = timedelta(hours=1)
    mail_results = list()
    for todo in todos:
        td = todo.expiration - now
        if zero < td <= an_hour:
            result = send_mail(
                subject=f'마감 알림 메일: {todo.title}',
                message=f"""아래 할일 마감이 1시간 남았습니다.
                제목: {todo.title}
                내용: {todo.content}
                기한: {todo.expiration}""",
                recipient_list=['joo2theeon@gmail.com'],
                from_email='',
            )
            mail_results.append(result)

    return mail_results


app.conf.beat_schedule = {
    'send test mail': {
        'task': 'send_notification_mail',
        'schedule': 600.0,
        'args': ()
    },
}
