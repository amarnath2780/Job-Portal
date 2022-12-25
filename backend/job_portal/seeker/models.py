from django.db import models
from accounts.models import Account
from superuser.models import Skill , CompanyCategory , CompanyDepartment
from recruiter.models import Job , RecruiterProfile ,Company

# Create your models here.
class SeekerProfile(models.Model):

    SEEKER_STATUS = [
        ('fresher' , 'Fresher'),
        ('intermediate' , 'Intermediate'),
        ('professional', 'Professional')
    ]


    seeker = models.ForeignKey(Account, related_name='seeker_profile',on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill , blank=True)
    profie_pic = models.ImageField('/images/' , blank=True)
    about = models.TextField(blank=True)
    category = models.ForeignKey(CompanyCategory,on_delete=models.CASCADE , blank=True , null=True , default=1)
    department = models.ForeignKey(CompanyDepartment ,on_delete=models.CASCADE , blank=True , null=True , default=1)
    level = models.CharField(default = 'fresher' ,choices=SEEKER_STATUS , max_length=200 ,blank=True )
    experince = models.IntegerField(blank=True,null=True,default=1)
    state = models.CharField(max_length=200 , blank = True)
    country = models.CharField(max_length=200,blank=True)


class AppliedJob(models.Model):

    job_id = models.ForeignKey(Job ,on_delete=models.CASCADE)
    recruiter_id = models.ForeignKey(Account ,on_delete=models.CASCADE)
    seeker_id = models.ForeignKey(SeekerProfile ,on_delete=models.CASCADE)
    company_id = models.ForeignKey(Company ,on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add = True)
    resume = models.FileField(upload_to='resume')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    is_shortlisted = models.BooleanField(default=False , blank=True)
    is_decline = models.BooleanField(default=False , blank=True)
    is_applied = models.BooleanField(default=True , blank=True)


class Notificaiton(models.Model):

    title = models.CharField(max_length=200)
    sender = models.ForeignKey(SeekerProfile ,related_name = 'notification',on_delete=models.CASCADE,null=True,blank=True,)
    receive=models.ForeignKey(RecruiterProfile,null=True,blank=True,related_name='user_revoker',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=264,null=True,blank=True,default="unread")
    type_of_notification=models.CharField(max_length=264,null=True,blank=True)

    
    def __str__(self):
        return self.title