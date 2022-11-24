from django.contrib import admin
from .models import RecruiterProfile , Company, Application , Job , Qualification , Requirements

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


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display= ['id','job_title'  , 'company']

@admin.register(Requirements)
class ReqRequirementAdmin(admin.ModelAdmin):
    list_display = ['id','title']

@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = ['id','title']