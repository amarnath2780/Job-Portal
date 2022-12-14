from rest_framework import serializers
from .models import RecruiterProfile, Company, Application, Job , AddRequest ,Qualification , AddRequestDepartment ,AddRequestSkill ,ShorlistedAppliedSeekers
from accounts.serializers import UserViewSerializer 
from superuser.serializers import CompanyCategorySerializer ,CompanyDepartmentSerializer 
from .models import UserMembership,SubscriptionPlan,MembershipsPurchaces ,OfferLetter

class RecruiterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruiterProfile
        fields = '__all__'


class RecruiterProfileSerializerGet(serializers.ModelSerializer):
    recruiter = UserViewSerializer(read_only=True , many=False)
    category = CompanyCategorySerializer(read_only=True , many=False)
    class Meta:
        model = RecruiterProfile
        fields = '__all__'



class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = '__all__'


class QualificationSeializer(serializers.ModelSerializer):

    class Meta:
        model = Qualification
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Application
        fields = '__all__'


class JobSerilizer(serializers.ModelSerializer):
    company_id = CompanySerializer(read_only=True ,)
    recruiter_id = UserViewSerializer(read_only=True ,)
    category = CompanyCategorySerializer(read_only=True ,)
    department = CompanyDepartmentSerializer(read_only=True)
    qualification = QualificationSeializer(read_only=True)
    class Meta:
        model = Job
        fields = '__all__'

class JobSerilizerPOST(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class AddRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = AddRequest
        fields = '__all__'


class AddRequestSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddRequestSkill
        fields = '__all__'

class AddRequestDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddRequestDepartment
        fields = '__all__'


class ShorlistedAppliedSeekersSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShorlistedAppliedSeekers
        fields = '__all__'


class ShorlistedAppliedSeekersSerializerGET(serializers.ModelSerializer):
    seeker_id = UserViewSerializer(read_only=True ,)
    company = CompanySerializer(read_only=True ,)
    job_id = JobSerilizer(read_only=True ,)
    class Meta: 
        model = ShorlistedAppliedSeekers
        fields = '__all__'


class UserMembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserMembership
        fields = '__all__'


class SubscriptionPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubscriptionPlan
        fields = '__all__'


class MembershipsPurchacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipsPurchaces
        fields = '__all__'



class OfferLetterSerializer(serializers.ModelSerializer):

    class Meta:
        model = OfferLetter
        fields = '__all__'
