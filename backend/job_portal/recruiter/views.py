from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from accounts.models import Account
from .models import Company, RecruiterProfile, Application
from .serializers import CompanySerializer, RecruiterProfileSerializer, ApplicationSerializer  , JobSerilizer , AddRequestSerializer , RecruiterProfileSerializerGet
from rest_framework import status
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from superuser.models import CompanyCategory
from superuser.serializers import CompanyCategorySerializer
from .serializers import AddRequestSkillSerializer ,AddRequestDepartmentSerializer
from seeker.serializers import AppliedJobsSerizlizer
from seeker.models import AppliedJob
from recruiter.models import Job
# Create your views here.


class CompanyCategoryView(ModelViewSet):
    queryset = CompanyCategory.objects.all()
    serializer_class = CompanyCategorySerializer


class CompanyView(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class ApplyedJobsView(ModelViewSet):
    queryset = AppliedJob.objects.all()
    serializer_class = AppliedJobsSerizlizer


class CompanyAddView(APIView):
    def post(self, request:Response):
        serilizer = CompanySerializer(data = request.data)
        
        if serilizer.is_valid():
            print('serilizer is valid')
            serilizer.save()
            return Response({'message' : "company add successfully"} , status=status.HTTP_200_OK)
        else:
            print('serilzer is not valid')
            print(serilizer.errors)
            return Response({'message' : 'Details is not valid'} , status=status.HTTP_400_BAD_REQUEST)



class RecruiterProfileView(ModelViewSet):
    queryset = RecruiterProfile.objects.all()
    serializer_class = RecruiterProfileSerializer


class ApplicationView(APIView):
    def post(self , request:Response):

        id = request.query_params['id']

        serilizer = ApplicationSerializer(data=request.data)
        comapny_id = request.data.get('company')
        security_code = request.data.get('pass')
        users = request.data.get('email')

        recruiter = Account.objects.get(email =users)
        request.data['recruiter'] = recruiter.id
        company = Company.objects.get(id=comapny_id)

        if company.security_code == security_code:
            if serilizer.is_valid():
                serilizer.save()

                profile = RecruiterProfile.objects.get(id=id)

                if profile:
                    profile.is_requested = True

                    profile.save()

                return Response({'message' : "created successfully"  }, status=status.HTTP_200_OK)
            else:
                print(serilizer.errors)
                print('serilzer not valid')
                return Response({'message' : 'Details are not  Valid'} , status=status.HTTP_400_BAD_REQUEST )
        else:
            print('security code not valid')
            return Response({'message' : 'Company already exists'} , status=status.HTTP_400_BAD_REQUEST )

class ListCompanyView(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class ApplyedView(APIView):

    def get(self, request ,*awags , **kawags):

        try:
            id = request.query_params['id']
            application = Application.objects.filter(recruiter=id)
            serializer = ApplicationSerializer(application , many=True)

            return Response(data=serializer.data,status=status.HTTP_200_OK)
        except:
            print(serializer.errors)
            print('data not found')
            return Response({'message' : 'data not found'} , status=status.HTTP_400_BAD_REQUEST)

class PostJob(APIView):

    def post(self, request:Response):
        
        serializer = JobSerilizer(data=request.data)

        if serializer.is_valid():
            print('serilalizer is valid')
            serializer.save()
            return Response({'message' : "Job Posed successfully"  }, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            print('serilzer not valid')
            return Response({'message' : 'Details are not  Valid'} , status=status.HTTP_400_BAD_REQUEST )


class RequestCatAddView(APIView):

    def post(self, request:Response):

        serializer = AddRequestSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message' : "Add Category Request successfull"  }, status=status.HTTP_200_OK)
        else:
            print('serilzer not valid')
            print(serializer.errors)
            return Response({'message' : 'Details are not  Valid'} , status=status.HTTP_400_BAD_REQUEST )

class RequestSkillAddView(APIView):

    def post(self, request:Response):

        serializer = AddRequestSkillSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message' : "Add Skill Request successfull"  }, status=status.HTTP_200_OK)
        else:
            print('serilzer not valid')
            print(serializer.errors)
            return Response({'message' : 'Details are not  Valid'} , status=status.HTTP_400_BAD_REQUEST )

class RequestDepartmentAddView(APIView):

   def post(self, request:Response):
        serializer = AddRequestDepartmentSerializer(data=request.data)

        if serializer.is_valid():
            print('valid serilizer')
            print(serializer)
            serializer.save()
            print('saved')
            return Response({'message':'Add Department Request successfull'} , status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response({'message':' Data not found'} , status=status.HTTP_400_BAD_REQUEST)

class RecruiterProfileDetails(APIView):

    def get(self, request:Response):

        id  = request.query_params['id']

        try:
            profile = RecruiterProfile.objects.get(id=id)
            serializer = RecruiterProfileSerializerGet(profile , many=False)
            return Response(data=serializer.data , status=status.HTTP_200_OK)
        except:
            print('data not fount')
            return Response({'Message' : 'Data not found'} , status=status.HTTP_400_BAD_REQUEST)

class RecruiterUpdateProfile(APIView):

    def put(self, request:Response):
        id = request.query_params['id']

        profile = RecruiterProfile.objects.get(id=id)
        serilaizer = RecruiterProfileSerializer(instance=profile , data=request.data)

        if serilaizer.is_valid():
            serilaizer.save()
            return Response({"message":"changed the data"},status=status.HTTP_200_OK)
        else:
            print(serilaizer.errors)
            return Response({'message' : 'data not found'} , status=status.HTTP_400_BAD_REQUEST)



class ShortlistSeeker(APIView):

    def post(self, request:Response):

        id = request.query_params['id']
        uid = request.query_params['uid']

        seeker = AppliedJob.objects.get(id=id , seeker_id=uid)
        if seeker:
            seeker.is_shortlisted = True
            seeker.save()
            return Response({'message': "Added to shortlist"}, status=status.HTTP_200_OK)
        else:
            return Response({'Message' : 'Data not found'} , status=status.HTTP_400_BAD_REQUEST)


class JobAppliedSeekerView(APIView):

    def get(self, request:Response):

        try:
            id = request.query_params['id']

            job = AppliedJob.objects.filter(job_id=id)

            serilizer = AppliedJobsSerizlizer(job, many=True)

            return Response(data=serilizer.data ,status=status.HTTP_200_OK)
        except:
            print('data not found')
            return Response({'message' : 'Data not Found'} , status=status.HTTP_400_BAD_REQUEST)

class PostedJobListView(APIView):

    def get(self, request:Response):

        try:
            id = request.query_params['id']

            jobs = Job.objects.filter(recruiter=id)
            serializer = JobSerilizer(jobs , many=True)

            return Response(data= serializer.data , status=status.HTTP_200_OK)
        except:
            print('data not found')
            return Response({'message' : 'Data not Found'} , status=status.HTTP_400_BAD_REQUEST)


class AppliedJobSingleJob(APIView):

    def get(self, request:Response):

        try:
            id = request.query_params['id']

            job = AppliedJob.objects.get(id=id)
            serializer = AppliedJobsSerizlizer(job , many=False)

            return Response(data= serializer.data , status=status.HTTP_200_OK)
        except:
            print('data not found')
            return Response({'message' : 'Data not Found'} , status=status.HTTP_400_BAD_REQUEST)



class DeclineJobRequestView(APIView):

    def post(self, request):

        id = request.query_params['id']
        uid = request.query_params['uid']

        application = AppliedJob.objects.get(id=id ,  seeker_id=uid)

        if application:

            return Response({'message': "Request Declined"}, status=status.HTTP_200_OK)
        else:
            return Response({'Message' : 'Data not found'} , status=status.HTTP_400_BAD_REQUEST)
