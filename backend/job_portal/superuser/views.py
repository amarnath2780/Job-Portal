from django.shortcuts import render
from .models import CompanyCategory, Skill , CompanyDepartment , CompanyCategory
from .serializers import CompanyCategorySerializer , SkillSerializer ,CompanyDepartmentSerializer , CompanyCategorySerializer
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from recruiter.models import Application
from recruiter.serializers import ApplicationSerializer
from rest_framework.decorators import api_view, permission_classes
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

class ListCompanyCategoryView(ModelViewSet):
    queryset = CompanyCategory.objects.all()
    serializer_class = CompanyCategorySerializer

class PendingApp(ModelViewSet):
    queryset = Application.objects.filter(status="Pending")
    serializer_class = ApplicationSerializer

class AccepetdView(ModelViewSet):
    queryset = Application.objects.filter(status="Approved")
    serializer_class = ApplicationSerializer

class RejectedView(ModelViewSet):
    queryset = Application.objects.filter(status="Rejected")
    serializer_class = ApplicationSerializer

class CategoryAddView(APIView):

    def post(self , request:Response):
        serializer = CompanyCategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message':' added Successfully'} , status=status.HTTP_200_OK)
        else:
            print('serializer is not valid')
            print(serializer.errors)
            return Response({'message' : 'Category is invalid '} , status=status.HTTP_400_BAD_REQUEST)


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

@api_view(['PUT'])
def edit_appA(request, id):
    print(id)
    edit = Application.objects.get(id=id)
    print(edit)
    change = ApplicationSerializer(instance=edit, data=request.data)
    print(change)
    if change.is_valid():
        print('chnage is valid')
        change.save()
        return Response({"message":"changed the data"},status=status.HTTP_200_OK)
    else:
        print (change.errors)
        return Response({'message' : 'data not found'} , status=status.HTTP_400_BAD_REQUEST)

class ChangeStatus(APIView):

    def put(self , request:Response ,pk=None):
        id = request.query_params['id']
        print(id)
        edit = Application.objects.get(id=id)
        change = ApplicationSerializer(instance=edit, data=request.data)

        if change.is_valid():
            print('chnage is valid')
            change.save()
            return Response({"message":"changed the data"},status=status.HTTP_200_OK)
        else:
            return Response({'message' : 'data not found'} , status=status.HTTP_400_BAD_REQUEST)

class AddCategory(APIView):

    def Post(self, request:Response):
        serializer = CompanyCategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message':' added Successfully'} , status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response({'message':' Data not found'} , status=status.HTTP_400_BAD_REQUEST)


class AddDepartment(APIView):

    def post(self, request:Response):
        serializer = CompanyDepartmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message':' added Successfully'} , status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response({'message':' Data not found'} , status=status.HTTP_400_BAD_REQUEST)