from rest_framework.viewsets import ModelViewSet
from .models import SeekerProfile
from .serializers import SeekerProfileSerializer

# Create your views here.
class SeekerProfileViewSet(ModelViewSet):
    queryset = SeekerProfile.objects.all()
    serializer_class = SeekerProfileSerializer
