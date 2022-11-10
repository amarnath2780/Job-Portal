from rest_framework import serializers
from .models import RecruiterProfile, Company


class RecruiterProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecruiterProfile
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'