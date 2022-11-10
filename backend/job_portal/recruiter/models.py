from django.db import models
from accounts.models import Account
from superuser.models import CompanyCategory
# Create your models here.


class Company(models.Model):
    company_name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(CompanyCategory, on_delete=models.PROTECT)
    company_logo = models.ImageField(upload_to=f'media/{company_name}/logo', blank=True)
    started_date = models.DateField(blank=True, null=True)
    about = models.TextField(max_length=3000, blank=True)
    founder = models.CharField(max_length=200, blank=True)
    ceo_name = models.CharField(max_length=200, blank=True)
    ceo_image = models.ImageField(upload_to=f'media/{company_name}/ceo', blank=True)
    head_office_location = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.company_name





class RecruiterProfile(models.Model):
    recruiter = models.ForeignKey(Account ,related_name='recruiter_profile' , on_delete=models.CASCADE)
    company = models.ForeignKey(Company , on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.id)