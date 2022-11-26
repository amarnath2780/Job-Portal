from django.db import models
from accounts.models import Account
from superuser.models import Skill , CompanyCategory

# Create your models here.
class SeekerProfile(models.Model):
    seeker = models.ForeignKey(Account, related_name='seeker_profile',on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill , blank=True)
    profie_pic = models.ImageField('/images/' , blank=True)
    about = models.TextField(blank=True)
    category = models.ForeignKey(CompanyCategory,on_delete=models.CASCADE , blank=True)
    state = models.CharField(max_length=200 , blank = True)
    country = models.CharField(max_length=200,blank=True)


