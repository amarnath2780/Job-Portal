from celery import shared_task
from accounts.models import Account 
from django.core.mail import send_mail
from job_portal import settings

@shared_task(bind=True)
def test_func(self):
    print('Hello world')
    return 'Done'


@shared_task(bind=True)
def send_mail_func(self ,id):

    user = Account.objects.get(id='3')

    mail_subject = "The celery is working dude"
    message = "The celery is working now "

    to_email = user.email

    send_mail(
        subject=mail_subject,
        message=message,
        from_email= settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=True,
    )
    
    return 'Done'