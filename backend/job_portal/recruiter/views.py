from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from accounts.models import Account
from .models import Company, RecruiterProfile, Application
from .serializers import CompanySerializer, RecruiterProfileSerializer, ApplicationSerializer 
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# Create your views here.


class CompanyView(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyAddView(APIView):
    def post(self, request):
        serilizer = CompanySerializer(data = request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'message' : "company add successfully"} , status=status.HTTP_200_OK)
        else:
            print('serilzer is valid')
            print(serilizer.errors)
            return Response({'message' : 'Details is not valid'} , status=status.HTTP_400_BAD_REQUEST)



class RecruiterProfileView(ModelViewSet):
    queryset = RecruiterProfile.objects.all()
    serializer_class = RecruiterProfileSerializer


class ApplicationView(APIView):
    def post(self , request:Response):

        serilizer = ApplicationSerializer(data=request.data)
        comapny_id = request.data.get('company')
        security_code = request.data.get('pass')
        users = request.data.get('email')

        recruiter = Account.objects.get(email =users)
        print(recruiter.id)
        request.data['recruiter'] = recruiter.id
        company = Company.objects.get(id=comapny_id)
        print(f'code{company.security_code}')

        if company.security_code == security_code:
            if serilizer.is_valid():
                serilizer.save()
                return Response({'message' : "created successfully" } , status=status.HTTP_200_OK)
            else:
                print('serilzer not valid')
                return Response({'message' : 'Details are not  Valid'} , status=status.HTTP_400_BAD_REQUEST )
        else:
            print('security code not valid')
            return Response({'message' : 'Security Code Not Valid'} , status=status.HTTP_400_BAD_REQUEST )

class ListCompanyView(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


