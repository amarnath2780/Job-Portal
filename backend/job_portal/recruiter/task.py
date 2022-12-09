from celery import shared_task
from accounts.models import Account 
from django.core.mail import send_mail
from job_portal import settings
from recruiter.models import ShorlistedAppliedSeekers

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