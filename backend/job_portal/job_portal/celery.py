from __future__ import absolute_import , unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab  


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_portal.settings')

app = Celery('job_portal')
app.conf.enable_utc = False


app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')


#CELERY BEAT SETTING
app.conf.beat_schedule = {
    # 'send-mail-at-8AM': {
    #     'task' : 'recruiter.task.send_mail_func',
    #     'schedule' : crontab(hour=15, minute=10),
    #     # 'args': ()
    # }
}



app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request{self.requsest!r}')