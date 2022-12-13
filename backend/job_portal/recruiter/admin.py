from django.contrib import admin
from .models import RecruiterProfile , Company, Application , Job , Qualification , Requirements ,AddRequest ,AddRequestSkill ,AddRequestDepartment ,ShorlistedAppliedSeekers
from .models import UserMembership,SubscriptionPlan,MembershipsPurchaces , OfferLetter
# Register your models here.

@admin.register(RecruiterProfile)
class RecruiterProfileAdmin(admin.ModelAdmin):
    list_display = [ 'id','recruiter', 'company']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'id', 'founder', 'ceo_name', 'head_office_location']


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id','first_name'  , 'status']


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display= ['id','job_title'  , 'company_id']

@admin.register(Requirements)
class ReqRequirementAdmin(admin.ModelAdmin):
    list_display = ['id','title']

@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = ['id','title']


@admin.register(AddRequest)
class AddRequestAdmin(admin.ModelAdmin):
    list_display = ['id' , 'category_name']


@admin.register(AddRequestSkill)
class AddRequestSkillAdmin(admin.ModelAdmin):
    list_display = ['id' , 'skill_name' , 'department_id']


@admin.register(AddRequestDepartment)
class AddRequestDepartmentAdmin(admin.ModelAdmin):
    list_display = ['id' , 'category_id' , 'department_name']


@admin.register(ShorlistedAppliedSeekers)
class ShorlistedAppliedSeekersAdmin(admin.ModelAdmin):
    list_display = ['id' , 'job_id' , 'seeker_id']


@admin.register(UserMembership)
class UserMembershipAdmin(admin.ModelAdmin):
    list_display = ['id', 'title' , 'duration','price']



@admin.register(SubscriptionPlan)
class UserMembershipAdmin(admin.ModelAdmin):
    list_display = ['id', 'user' , 'plan_expires_in','paid']


@admin.register(MembershipsPurchaces)
class UserMembershipAdmin(admin.ModelAdmin):
    list_display = ['id', 'user' , 'membership']


@admin.register(OfferLetter)
class OfferLetterAdmin(admin.ModelAdmin):
    list_display = ['id', 'user' , 'job' , 'recruiter']