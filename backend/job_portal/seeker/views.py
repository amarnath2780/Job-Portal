from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import SeekerProfile 
from .serializers import SeekerProfileSerializer  , AppliedJobsSerizlizer,AppliedJobsSerizlizerPost ,SeekerProfileSerializerGet
from recruiter.models import Job ,RecruiterProfile
from recruiter.serializers import JobSerilizer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FileUploadParser , MultiPartParser ,FormParser
from accounts.models import Account
from accounts.serializers import UserViewSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .filter import JobFilter
from rest_framework import filters

# Create your views here.
class SeekerProfileViewSet(ModelViewSet):
    queryset = SeekerProfile.objects.all()
    serializer_class = SeekerProfileSerializer



    
class ViewJobSingle(APIView):

    def get(self, request):
        
        id = request.query_params['id']
        print(id)
          
        job = Job.objects.get(id=id)

        serializer = JobSerilizer(job, many=False)

        return Response(data=serializer.data,status=status.HTTP_200_OK)




class UpdateProfile(APIView):

    def put(self, request:Response):
        id = request.query_params['id']

        profile = SeekerProfile.objects.get(id=id)
        serilaizer = SeekerProfileSerializer(instance=profile , data=request.data)

        if serilaizer.is_valid():
            serilaizer.save()
            return Response({"message":"changed the data"},status=status.HTTP_200_OK)
        else:
            print(serilaizer.errors)
            return Response({'message' : 'data not found'} , status=status.HTTP_400_BAD_REQUEST)



class ViewProfile(APIView):

    def get(self , request:Response):
        try:
            id = request.query_params['id']

            profile = SeekerProfile.objects.get(id=id)

            serializer = SeekerProfileSerializerGet(profile, many=False)

            return Response(data=serializer.data,status=status.HTTP_200_OK)
        except:
            print('data not found')
            return Response({'message' : 'data not found'} , status=status.HTTP_400_BAD_REQUEST)


class UserDetails(APIView):


    def get(self, request:Response):
        try:
            id = request.query_params['id']

            profile = Account.objects.get(id=id)
            
            serializer = UserViewSerializer(profile , many=False)

            return Response(data=serializer.data,status=status.HTTP_200_OK)
        except:
            print('data not found')
            return Response({'message' : 'data not found'} , status=status.HTTP_400_BAD_REQUEST)



class ViewAllJobs(APIView):

    def get(self,request:Response):

        try:
            job = Job.objects.all()

            serializer = JobSerilizer(job , many=True)

            return Response(data=serializer.data,status=status.HTTP_200_OK)
        except:
            print('data not found')
            return Response({'message' : 'data not found'} , status=status.HTTP_400_BAD_REQUEST)




class ApplyJob(APIView):

    def post(self, request:Response):


        serializer = AppliedJobsSerizlizerPost(data=request.data)
        users = request.data.get('recruiter')
        print(users)
        recruiter = Account.objects.get(email =users)
        print(recruiter)
        request.data['recruiter_id'] = recruiter.id

        if serializer.is_valid():

            print('serializer is valid')
            serializer.save()
            return Response({'Message':'Applied Successfully'} , status=status.HTTP_200_OK)
        else:
            print('data not found')
            print(serializer.errors)
            return Response({'Message':'Data not Found'} , status=status.HTTP_400_BAD_REQUEST)



class JobFilerView(ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerilizer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = JobFilter

class SearchBarFilter(ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerilizer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^job_title']