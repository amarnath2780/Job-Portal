from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import SeekerProfile
from .serializers import SeekerProfileSerializer
from recruiter.models import Job
from recruiter.serializers import JobSerilizer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class SeekerProfileViewSet(ModelViewSet):
    queryset = SeekerProfile.objects.all()
    serializer_class = SeekerProfileSerializer


class ViewAllJobs(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerilizer
    
class ViewJobSingle(APIView):

    def get(self, request):

        try:
            id = request.query_params['id']

            job = Job.objects.get(id=id)

            serializer = JobSerilizer(job, many=False)

            return Response(data=serializer.data,status=status.HTTP_400_BAD_REQUEST)
        except:
            print('data not found')
            return Response({'message' : 'data not found'} , status=status.HTTP_400_BAD_REQUEST)