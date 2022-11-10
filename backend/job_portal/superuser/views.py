from django.shortcuts import render
from .models import CompanyCategory
from .serializers import CompanyCategorySerializer
from rest_framework.viewsets import GenericViewSet, ModelViewSet

# Create your views here.


class CompanyCategoryView(ModelViewSet):
    queryset = CompanyCategory.objects.all()
    serializer_class = CompanyCategorySerializer