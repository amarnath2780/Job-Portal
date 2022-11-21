from django.urls import path,include
from recruiter.views import ApplicationView , CompanyAddView , CompanyView , ListCompanyView ,CompanyCategoryView, ApplyedView,RecruiterProfileView
from rest_framework import routers
from accounts.views import SeekerView , RecruiterView
from superuser.views import ListSkillView , SkillAddView ,ListCompanyDepartmentView , ListCompanyCategoryView , CategoryAddView
from superuser.views import edit_appA

router = routers.DefaultRouter()
router.register(r'view-company', CompanyView , basename="view-company")
router.register(r'company-list' , ListCompanyView , basename="list-company" )
router.register(r'company-category' , CompanyCategoryView , basename='view-company-category')
router.register(r'recruiter', RecruiterProfileView, basename='recruiter')
router.register(r'view-seeker', SeekerView, basename='seekers')
router.register(r'view-recruiters', RecruiterView , basename='recruiters-list')
router.register(r'list-skills', ListSkillView , basename='list-skills')
router.register(r'list-department', ListCompanyDepartmentView , basename='list-department')
router.register(r'list-category', ListCompanyCategoryView , basename='list-department')


urlpatterns = [
    path('user/', include('accounts.urls')),
    path('application/' , ApplicationView.as_view() , name="application"),
    path('add-company/', CompanyAddView.as_view() , name="company_add"),
    path('view-app/', ApplyedView.as_view() , name="applied-view"),
    path('view-app/', ApplyedView.as_view() , name="applied-view"),
    path('add-skill/' , SkillAddView.as_view() , name='add-skill'),
    path('add-category/' , CategoryAddView.as_view() , name='add-category'),
    path('edit_app/<int:id>/', edit_appA, name="edit_appA"),

]

urlpatterns += router.urls