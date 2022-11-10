from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Company, RecruiterProfile
from .serializers import CompanySerializer, RecruiterProfileSerializer

# Create your views here.


class CompanyView(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class RecruiterProfileView(ModelViewSet):
    queryset = RecruiterProfile.objects.all()
    serializer_class = RecruiterProfileSerializer
    