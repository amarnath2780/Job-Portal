from django.contrib import admin
from .models import CompanyCategory, CompanyDepartment, Skill


@admin.register(CompanyCategory)
class CompanyCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'id']


@admin.register(CompanyDepartment)
class CompanyDepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_name', 'category']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['skill_name', 'department']