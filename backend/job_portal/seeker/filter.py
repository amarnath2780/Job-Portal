import django_filters
from recruiter.models import Job



class JobFilter(django_filters.FilterSet):
    class Meta:
        model = Job
        fields = ['job_title','category','department','level','experience']