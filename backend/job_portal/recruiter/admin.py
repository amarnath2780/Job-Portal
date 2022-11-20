from django.contrib import admin
from .models import RecruiterProfile , Company, Application

# Register your models here.

@admin.register(RecruiterProfile)
class RecruiterProfileAdmin(admin.ModelAdmin):
    list_display = ['recruiter', 'company']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'id', 'founder', 'ceo_name', 'head_office_location']


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id','first_name'  , 'status']