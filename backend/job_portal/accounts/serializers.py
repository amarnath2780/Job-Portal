import re
from rest_framework import serializers
from .models import Account
from rest_framework.validators import ValidationError



class SignUpSerializer(serializers.ModelSerializer):
    
    class Meta:
        model  = Account
        fields = ('first_name', 'middle_name' , 'last_name' , 'email' , 'role' , 'dob' , 'phone_number' , 'password')


    def validate(self, attrs):
        # email validation
        email_exist = Account.objects.filter(email=attrs['email']).exists()

        if email_exist:
            return ValidationError('This email is already exist')
        return super().validate(attrs)

    def validate_email(self, value):

        pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"

        if not re.match(pat,value):
            raise serializers.ValidationError("This is not a valid email, try again!")

        return value

    def create(self, validated_data):
        # hashing password
        password = validated_data.pop('password')

        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['first_name', 'middle_name', 'last_name', 'role', 'phone_number', 'email', 'dob', 'city', 'profile_image']





