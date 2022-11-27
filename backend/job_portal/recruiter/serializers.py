from rest_framework import serializers
from .models import RecruiterProfile, Company, Application, Job , AddRequest
from accounts.serializers import UserViewSerializer

class RecruiterProfileSerializer(serializers.ModelSerializer):
    recruiter = UserViewSerializer(read_only=True , many=False)
    class Meta:
        model = RecruiterProfile
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Application
        fields = '__all__'


class JobSerilizer(serializers.ModelSerializer):
    company_id = CompanySerializer(read_only=True ,)
    recruiter = UserViewSerializer(read_only=True ,)
    class Meta:
        model = Job
        fields = '__all__'


class AddRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = AddRequest
        fields = '__all__'