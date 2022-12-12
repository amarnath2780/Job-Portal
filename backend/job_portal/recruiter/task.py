from celery import shared_task
from accounts.models import Account 
from django.core.mail import send_mail
from job_portal import settings
from datetime import datetime
from recruiter.models import ShorlistedAppliedSeekers , SubscriptionPlan,RecruiterProfile

@shared_task(bind=True)
def test_func(self):
    print('Hello world')
    return 'Done'


@shared_task(bind=True)
def send_mail_func(self,id):

    users = ShorlistedAppliedSeekers.objects.filter(job_id = id, send = False)

    for user in users:
        print(user)
        mail_subject = f"You get Shortlisted for  {user.job_id.job_title}"
        message = f"Hey {user.seeker_id.first_name} , We are happy to inform you that you are shortlisted for {user.job_id.job_title}. The recruiter will contact you shorly"

        to_email = user.seeker_id.email

        print(to_email)

        send_mail(
            subject=mail_subject,
            message=message,
            from_email= settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
        user.send = True
        user.save()
    
    return 'Done'


@shared_task(bind=True)
def update_paid(self):
    
    instance = SubscriptionPlan.objects.all()

    today = datetime.now().date()

    for sub in instance:
        if sub.plan_expires_in < today:
            user = RecruiterProfile.objects.get(id=sub.user.user.id)
            user.paid = False
            user.save()
            instance.delete()
        else:
            sub.paid = True
            user = RecruiterProfile.objects.get(id=sub.user.user.id)
            user.paid = True
            user.save()

    return 'Done'

@shared_task(bind=True)
def send_reminder_mail(self):

    users = Account.objects.filter(role = 'seeker')

    for user in users:
        print(user)
        mail_subject = f"How Are you  {user.first_name}"
        message =  f"Hey {user.first_name} ,  In TrabaJo many new jobs are added by new recruiters please check and apply and upgrade you life to a next level get better salary and a better life style we support for that. Thank You...... "

        to_email = user.email

        print(to_email)

        send_mail(
            subject=mail_subject,
            message=message,
            from_email= settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
        print(f'mail send {to_email}')
    
    return 'Done'
