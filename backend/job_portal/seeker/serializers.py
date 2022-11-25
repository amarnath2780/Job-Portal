from rest_framework import serializers
from .models import SeekerProfile 


class SeekerProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = SeekerProfile
        fields = '__all__'
