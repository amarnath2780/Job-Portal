from rest_framework import generics
from .serializers import SignUpSerializer
from rest_framework.permissions import  AllowAny
from rest_framework.request import Request

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
            