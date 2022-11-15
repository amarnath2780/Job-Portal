from rest_framework import serializers
from .models import RecruiterProfile, Company, Application


class RecruiterProfileSerializer(serializers.ModelSerializer):

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