from django.contrib import admin
from .models import CompanyCategory, CompanyDepartment, Skill ,AdminProfile


@admin.register(CompanyCategory)
class CompanyCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'id']


@admin.register(CompanyDepartment)
class CompanyDepartmentAdmin(admin.ModelAdmin):
    list_display = ['id','department_name', 'category']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id','skill_name', 'department']


@admin.register(AdminProfile)
class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ['id','admin']