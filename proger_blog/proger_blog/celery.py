import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proger_blog.settings')

app = Celery('proger_blog')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# запуск по времени
app.conf.beat_schedule = {
    'send-spam-every-1-minute': {
        'task': 'email_send.tasks.send_beat_email',
        'schedule': crontab(minute='*/1')   # задаем переодичность
    }
}