from rest_framework import serializers
from .models import SeekerProfile 
from accounts.serializers import UserViewSerializer

class SeekerProfileSerializer(serializers.ModelSerializer):
    seeker = UserViewSerializer(read_only = True , many=False)
    class Meta:
        model = SeekerProfile
        fields = '__all__'
