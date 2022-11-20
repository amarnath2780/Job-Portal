from rest_framework import generics
from .serializers import SignUpSerializer, UserViewSerializer
from rest_framework.permissions import  AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from accounts.models import Account
from seeker.models import SeekerProfile
from recruiter.admin import RecruiterProfile
from superuser.models import AdminProfile
from rest_framework.views import APIView 
from rest_framework.viewsets import ModelViewSet
from accounts.otp import send_otp,verify_otp
from django.contrib.auth import authenticate
from .token import create_jwt_pair_tokens



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
                phone_number = data.get('phone_number')
                # send_otp(phone_number)
                # print('otp send')
            elif role == 'recruiter':
                print('role is recruiter')
                user = Account.objects.get(email=email)
                user.is_staff = True
                user.save()
                RecruiterProfile.objects.create(recruiter=user)
                phone_number = data.get('phone_number')
                # send_otp(phone_number)
                # print('otp send')
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


class  Verify_otpView(APIView):

    def post(self, request : Request):
        data = request.data
        check_otp = data.get('otp')

        phone_number = data.get('phone_number')        
        check = verify_otp(phone_number,check_otp)

        if check:
            user = Account.objects.get(phone_number = phone_number)
            user.is_verified = True
            user.save()

            return Response(
                {'Success':'User is verified'},status=status.HTTP_200_OK)
        else:
            return Response({'Failed':'User is Not verified'},status=status.HTTP_400_BAD_REQUEST)



class LoginView(APIView):
    permission_classes =  [AllowAny]

    def post(self , request:Request):
        email = request.data.get('email')
        password = request.data.get('password') 
        print(email,password)
        user = authenticate(request, email=email, password=password)

        print(f'user is {user}')

        if user is not None:        
            print('authenticatied')
            tokens = create_jwt_pair_tokens(user) 
            profile = {}      

            if user.role == 'seeker':
                profile = SeekerProfile.objects.get(seeker=user)
            elif user.role == 'recruiter':
                profile = RecruiterProfile.objects.get(recruiter=user)
            else:
                profile = AdminProfile.objects.get(admin=user)

            response = {
                "message": "Login successfull",
                "token": tokens,
                "user" : {
                    "user_id":user.id,
                    "email":user.email,
                    "role":user.role,
                    'profile_id':profile.id
                }
            } 
            
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={
                "message": "Invalid email or password!"
            }, status=status.HTTP_400_BAD_REQUEST)



class UserView(generics.RetrieveAPIView):
    permission_classes = []
    serializer_class = UserViewSerializer
    queryset = Account.objects.all()


class SeekerView(ModelViewSet):
    queryset = Account.objects.filter(role='seeker')
    serializer_class = UserViewSerializer


class RecruiterView(ModelViewSet):
    queryset = Account.objects.filter(role='recruiter')
    serializer_class = UserViewSerializer