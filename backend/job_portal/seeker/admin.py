from django.contrib import admin
from seeker.models import SeekerProfile ,AppliedJob


@admin.register(SeekerProfile)
class SeekerProfileAdmin(admin.ModelAdmin):
    list_display = ('seeker', 'id',)
    
@admin.register(AppliedJob)
class AppliedJobsAdmin(admin.ModelAdmin):
    list_display = ('seeker_id' , 'recruiter_id' , 'job_id')