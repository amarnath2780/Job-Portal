from rest_framework import serializers
from .models import CompanyCategory ,CompanyDepartment,Skill , AdminProfile , Banner



class CompanyCategorySerializer(serializers.ModelSerializer):
   class Meta:
    model = CompanyCategory
    fields = '__all__'


class CompanyDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDepartment
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class AdminProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdminProfile
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banner
        fields = '__all__'