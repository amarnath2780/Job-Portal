from django.urls import path,include
from recruiter.views import ApplicationView , CompanyAddView , CompanyView , ListCompanyView ,CompanyCategoryView, ApplyedView,RecruiterProfileView
from rest_framework import routers
from accounts.views import SeekerView

router = routers.DefaultRouter()
router.register(r'view-company', CompanyView , basename="view-company")
router.register(r'company-list' , ListCompanyView , basename="list-company" )
router.register(r'company-category' , CompanyCategoryView , basename='view-company-category')
router.register(r'recruiter', RecruiterProfileView, basename='recruiter')
router.register(r'view-seeker', SeekerView, basename='seekers')


urlpatterns = [
    path('user/', include('accounts.urls')),
    path('application/' , ApplicationView.as_view() , name="application"),
    path('add-company/', CompanyAddView.as_view() , name="company_add"),
    path('view-app/', ApplyedView.as_view() , name="applied-view")
]

urlpatterns += router.urls