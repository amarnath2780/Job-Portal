from rest_framework import generics
from .serializers import SignUpSerializer
from rest_framework.permissions import  AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from accounts.models import Account
from seeker.models import SeekerProfile
from recruiter.admin import RecruiterProfile
# Create your views here.

class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]


    def post(self , request : Request):
        data = request.data
        print(data)

        serializer = self.serializer_class(data=data)

        role = request.data.get('role')
        email = request.data.get('email')

        if serializer.is_valid():
            serializer.save()
            
            print('serializer is valid')

            if role == 'seeker':
                print('role is seeker')
                user = Account.objects.get(email = email)
                SeekerProfile.objects.create(seeker=user)
            elif role == 'recruiter':
                print('role is recruiter')
                user = Account.objects.get(email=email)
                RecruiterProfile.objects.create(recruiter=user)
            else:
                print('user role is not user and recruiter But base User Created!')
            response = {
                'message': "User Created Successfully",
            }
            return Response(data=response,status=status.HTTP_201_CREATED)
        else:
            print('serializer is not valid')
            print(serializer.errors)
            return Response(data==serializer.errors , status=status.HTTP_400_BAD_REQUEST)



