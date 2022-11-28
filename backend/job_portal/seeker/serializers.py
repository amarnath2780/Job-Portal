from rest_framework import serializers
from .models import SeekerProfile , AppliedJob
from accounts.serializers import UserViewSerializer
from recruiter.serializers import JobSerilizer , RecruiterProfileSerializer

class SeekerProfileSerializer(serializers.ModelSerializer):
    seeker = UserViewSerializer(read_only = True , many=False)
    class Meta:
        model = SeekerProfile
        fields = '__all__'

class AppliedJobsSerizlizer(serializers.ModelSerializer):
    job = JobSerilizer(read_only = True , many=False)
    recruiter = RecruiterProfileSerializer(read_only = True , many=False)
    seeker = UserViewSerializer(read_only = True , many=False)
    class Meta:
        model = AppliedJob
        fields = '__all__'