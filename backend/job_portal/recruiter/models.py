from django.db import models
from accounts.models import Account
from superuser.models import CompanyCategory , CompanyDepartment
from django.db.models.signals import post_save ,pre_save
from django.dispatch import receiver
from datetime import datetime
from datetime import timedelta



# Create your models here.


class Company(models.Model):
    company_name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(CompanyCategory, on_delete=models.PROTECT)
    company_logo = models.ImageField(upload_to=f'media/{company_name}/logo', blank=True)
    started_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    about = models.TextField(max_length=3000, blank=True)
    founder = models.CharField(max_length=200, blank=True)
    ceo_name = models.CharField(max_length=200, blank=True)
    head_office_location = models.CharField(max_length=200, blank=True)
    security_code = models.CharField(max_length=100)


    def __str__(self):
        return self.company_name







class RecruiterProfile(models.Model):
    recruiter = models.ForeignKey(Account ,related_name='recruiter_profile' , on_delete=models.CASCADE)
    company = models.ForeignKey(Company , on_delete=models.CASCADE, null=True, blank=True)
    profie_pic = models.ImageField('/images/' , blank=True)
    about = models.TextField(blank=True)
    category = models.ForeignKey(CompanyCategory,on_delete=models.CASCADE , blank=True , null=True)
    state = models.CharField(max_length=200 , blank = True)
    country = models.CharField(max_length=200,blank=True)
    is_requested = models.BooleanField(default=False, blank=True)
    is_acceped =  models.BooleanField(default=False, blank=True)
    is_rejected = models.BooleanField(default=False, blank=True)
    paid = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return str(self.id)






class Application(models.Model):

    STATUS = [
        ('Pending', 'Pending'),
        ('Approved' , 'Approved'),
        ('Rejected' ,  'Rejected'),

    ]

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length = 200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    recruiter = models.ForeignKey(Account , on_delete=models.CASCADE , blank=True )
    company = models.OneToOneField(Company , on_delete=models.CASCADE,  blank=True)
    city  = models.CharField(max_length=100 , blank=True , null=True)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=200)
    status = models.CharField(default='Pending',choices=STATUS,max_length=300,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    

    def __str__(self):
        return self.first_name

class Qualification(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title




class Job(models.Model):

    SALARY_TYPE = [
        ('a month' , 'a month'),
        ('a year' ,  'a year'),
    ]

    JOB_TYPE = [
        ('part-time' , 'Part Time'),
        ('full-time' , 'Full Time'),
        ('intern' , 'Intern'),
        ('remort' , 'Remort'),
        ('work-from-home' , 'Work From Home'),
    ]

    LEVEL = [
        ('fresher' , 'Fresher'),
        ('intermediate' , 'Intermediate'),
        ('professional', 'Professional')
    ]

    job_title = models.CharField(max_length=200)
    company_id = models.ForeignKey(Company , on_delete=models.CASCADE)
    recruiter_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(CompanyCategory , on_delete=models.CASCADE , blank=True , null=True)
    department = models.ForeignKey(CompanyDepartment , on_delete=models.CASCADE , blank=True , null=True)
    level = models.CharField(default = 'fresher' ,choices=LEVEL , max_length=200 ,blank=True , null=True)
    experience = models.IntegerField(blank=True , null=True)
    min_salary = models.IntegerField(blank=True)
    max_salary = models.IntegerField()
    salary_type = models.CharField(default='a year' , choices=SALARY_TYPE, max_length = 200 , blank=True)
    job_type = models.CharField(default = 'full-time' ,choices=JOB_TYPE ,max_length = 200 , blank=True)
    qualification = models.ForeignKey(Qualification , on_delete=models.CASCADE, blank=True, null=True)
    full_discription = models.TextField(blank=True)
    short_discription = models.TextField(blank=True)
    schedule = models.CharField(blank=True , max_length=300 ,null=True)
    state =  models.CharField(blank=True , max_length=300)
    country =  models.CharField(blank=True , max_length=300)
    vacancy = models.IntegerField()
    urgent = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.job_title


class Requirements(models.Model):
    title = models.CharField(max_length=200)
    job = models.ForeignKey(Job , on_delete=models.CASCADE)
    requirement_2 = models.CharField(max_length=200 , blank=True)
    requirement_3 = models.CharField(max_length=200 , blank=True)
    requirement_4 = models.CharField(max_length=200 , blank=True)
    requirement_5 = models.CharField(max_length=200 , blank=True)

    def __str__(self):
        return self.title



class AddRequest(models.Model):
    category_name = models.CharField(max_length = 200)

    def __str__(self):
        return self.category_name

class AddRequestSkill(models.Model):
    skill_name = models.CharField(max_length = 200)
    department_id = models.ForeignKey(CompanyDepartment, on_delete=models.CASCADE)

    def __str__(self):
        return self.skill_name


class AddRequestDepartment(models.Model):
    category = models.ForeignKey(CompanyCategory, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=200)

    def __str__(self):
        return self.department_name

class ShorlistedAppliedSeekers(models.Model):
    seeker_id = models.ForeignKey(Account,on_delete=models.CASCADE)
    company = models.ForeignKey(Company ,on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job ,on_delete=models.CASCADE)  
    send = models.BooleanField(default = False , blank=True)


class UserMembership(models.Model):
    DURATION = (
        (30 , 'One Month'),
        (90 , 'Three Month'),
    )
    title = models.CharField(max_length=200 , default='Basic')
    duration = models.IntegerField(default=30 , choices=DURATION)
    price = models.CharField(max_length=200, default=0.00)

    def __str__(self):
        return self.title



class MembershipsPurchaces(models.Model):
    user = models.OneToOneField(RecruiterProfile , on_delete=models.CASCADE)
    membership = models.ForeignKey(UserMembership , on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user.recruiter.first_name

class SubscriptionPlan(models.Model):
    user = models.ForeignKey(MembershipsPurchaces , on_delete=models.CASCADE)
    plan_expires_in = models.DateField(null=True , blank=True)
    paid = models.BooleanField(default=True)


@receiver(post_save , sender=MembershipsPurchaces)
def create_subscription(sender, instance, *args , **kwargs):
    if instance:
        SubscriptionPlan.objects.create(user=instance ,  plan_expires_in=datetime.now().date()+ timedelta(days=instance.membership.duration) )
        profile = RecruiterProfile.objects.get(id=instance.user.id)
        profile.paid = True
        profile.save()


class OfferLetter(models.Model):
    user = models.ForeignKey(Account , on_delete=models.CASCADE)
    job = models.ForeignKey(Job , on_delete=models.CASCADE)
    recruiter = models.ForeignKey(RecruiterProfile , on_delete=models.CASCADE)
    salary = models.CharField(max_length=500)
    join_data = models.CharField(max_length=400)
    position = models.CharField(max_length=300)


    def __str__(self):
        return self.user.first_name
    
   