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
from recruiter.models import AddRequest ,AddRequestSkill ,AddRequestDepartment , RecruiterProfile
from recruiter.serializers import AddRequestSerializer,AddRequestDepartmentSerializer , AddRequestSkillSerializer , RecruiterProfileSerializer
from superuser.serializers import BannerSerializer
from superuser.models import Banner
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


class ViewAllReq(ModelViewSet):
    queryset = AddRequest.objects.all()
    serializer_class = AddRequestSerializer

class ViewSkillRequest(ModelViewSet):
    queryset = AddRequestSkill.objects.all()
    serializer_class = AddRequestSkillSerializer

class ViewDepartmentRequest(ModelViewSet):
    queryset = AddRequestDepartment.objects.all()
    serializer_class = AddRequestDepartmentSerializer




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
        edit = Application.objects.get(id=id)
        profile = RecruiterProfile.objects.get(recruiter = edit.recruiter)
        change = ApplicationSerializer(instance=edit, data=request.data)

        if change.is_valid():
            print('chnage is valid')
            change.save()
            
            profile.is_acceped = True
            profile.is_requested = False

            profile.save()

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


class EditSkill(APIView):

    def put(self, request:Response):
        id = request.query_params['id']
        
        skill = Skill.objects.get(id=id)
        serializer = SkillSerializer(instance=skill , data=request.data)

        if serializer.is_valid():
            print('serializer is valid')
            serializer.save()
            return Response({'message' : 'Skill changed Successfully'} , status=status.HTTP_200_OK)
        else:
            print('serializer is not valid')
            return Response({'Message' : 'Data is not valid'})


class EditCategory(APIView):

    def put(self, request:Response):
        id = request.query_params['id']

        category = CompanyCategory.objects.get(id=id)
        serializer = CompanyCategorySerializer(instance=category , data=request.data)

        if serializer.is_valid():
            print('serializer is valid')
            serializer.save()
            return Response({'Message': 'Category changed Successfully'})
        else:
            print(serializer.errors)
            return Response({'Messages': 'Data is not valid'})


class EditDepartment(APIView):

    def put(self, request:Response):
        id = request.query_params['id']


        department = CompanyDepartment.objects.get(id=id)
        serializer = CompanyDepartmentSerializer(instance=department , data=request.data)

        if serializer.is_valid():
            print('serilizer is valid')
            serializer.save()
            return Response({'Message': 'Department changed Successfully'})
        else:
            print(serializer.errors)
            return Response({'Messages': 'Data is not valid'})

class DeleteDepartment(APIView):

    def get(self, request):

        id = request.query_params['id']

        department = CompanyDepartment.objects.get(id=id)

        if department:
            department.delete()
            return Response({'Message': 'Department Deleted Successfully'})

class DeleteSkill(APIView):

    def get(self, request):

        id = request.query_params['id']

        skill = Skill.objects.get(id=id)

        if skill:
            skill.delete()
            return Response({'Message': 'Skill Deleted Successfully'})


class AddRequestCategory(APIView):

    def post(slef, request:Response):

        id = request.query_params['id']

        serializer = CompanyCategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            requested = AddRequest.objects.get(id=id)

            if requested:
                requested.delete()
            else:
                return Response({'message':' Data cant found'} , status=status.HTTP_400_BAD_REQUEST)
            return Response({'message':'Category added Successfully and remove the request'} , status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response({'message':' Data not found'} , status=status.HTTP_400_BAD_REQUEST)


class AddRequestSkillView(APIView):


    def post(self, request:Response):

        id = request.query_params['id']
        serializer = SkillSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            requested = AddRequestSkill.objects.get(id=id)

            if requested:
                requested.delete()
            else:
                return Response({'message':' Data cant found'} , status=status.HTTP_400_BAD_REQUEST)
            return Response({'message':'Category added Successfully and remove the request'} , status=status.HTTP_200_OK)

        else:
            print(serializer.errors)
            return Response({'message':' Data not found'} , status=status.HTTP_400_BAD_REQUEST)


class AddRequestDepartmentView(APIView):

    def post(self, request:Response):

        id = request.query_params['id']
        serializer = CompanyDepartmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            requested = AddRequestDepartment.objects.get(id=id)

            if requested:
                requested.delete()
            else:
                return Response({'message':' Data cant found'} , status=status.HTTP_400_BAD_REQUEST)
            return Response({'message':'Category added Successfully and remove the request'} , status=status.HTTP_200_OK)

        else:
            print(serializer.errors)
            return Response({'message':' Data not found'} , status=status.HTTP_400_BAD_REQUEST)


class BannerImageView(APIView):

    def get(self, request):

        id = request.query_params['id']

        banner = Banner.objects.get(id=id)

        serializer = BannerSerializer(banner , many=False)

        return Response(data=serializer.data , status=status.HTTP_200_OK)