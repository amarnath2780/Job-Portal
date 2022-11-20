from django.shortcuts import render
from .models import CompanyCategory, Skill , CompanyDepartment
from .serializers import CompanyCategorySerializer , SkillSerializer ,CompanyDepartmentSerializer
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class CompanyCategoryView(ModelViewSet):
    queryset = CompanyCategory.objects.all()
    serializer_class = CompanyCategorySerializer


class ListSkillView(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ListCompanyDepartmentView(ModelViewSet):
    queryset = CompanyDepartment.objects.all()
    serializer_class = CompanyDepartmentSerializer


class SkillAddView(APIView):

    def post(self, request:Response):
        serializer = SkillSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Skill added Successfully'} , status=status.HTTP_200_OK)
        else:
            print('serializer is not valid')
            print(serializer.errors)
            return Response({'message' : 'Skill is invalid '} , status=status.HTTP_400_BAD_REQUEST)