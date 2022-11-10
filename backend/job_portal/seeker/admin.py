from django.contrib import admin
from seeker.models import SeekerProfile


@admin.register(SeekerProfile)
class SeekerProfileAdmin(admin.ModelAdmin):
    list_display = ('seeker', 'id',)
    
