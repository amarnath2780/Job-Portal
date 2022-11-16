from django.urls import path,include
from recruiter.views import ApplicationView , CompanyAddView , CompanyView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'view-company', CompanyView , basename="view-company")

urlpatterns = [
    path('user/', include('accounts.urls')),
    path('app/' , ApplicationView.as_view() , name="application"),
    path('add-company/', CompanyAddView.as_view() , name="company_add"),
]

urlpatterns += router.urls