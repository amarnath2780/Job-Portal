from django.urls import path,include
from recruiter.views import ApplicationView , CompanyAddView , CompanyView , ListCompanyView ,CompanyCategoryView, ApplyedView,RecruiterProfileView
from rest_framework import routers
from accounts.views import SeekerView , RecruiterView
from superuser.views import ListSkillView , SkillAddView ,ListCompanyDepartmentView , ListCompanyCategoryView , CategoryAddView ,PendingApp,ChangeStatus , AccepetdView , RejectedView,AddDepartment
from superuser.views import edit_appA
from superuser.views import EditSkill , EditCategory, EditDepartment ,DeleteDepartment,DeleteSkill ,ViewAllReq,AddRequestCategory
from recruiter.views import PostJob , RequestCatAddView , RecruiterProfileDetails
from seeker.views import ViewAllJobs , ViewJobSingle , UpdateProfile , ViewProfile , UserDetails, ApplyJob ,JobFilerView

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
router.register(r'pending-app', PendingApp , basename='pending-app')
router.register(r'accepted-app', AccepetdView , basename='acceped-app')
router.register(r'rejected-app', RejectedView , basename='rejected-app')
router.register(r'request-category', ViewAllReq , basename='add-req-cat')




urlpatterns = [
    path('user/', include('accounts.urls')),
    path('application/' , ApplicationView.as_view() , name="application"),
    path('add-company/', CompanyAddView.as_view() , name="company_add"),
    path('view-app/', ApplyedView.as_view() , name="applied-view"),
    path('view-app/', ApplyedView.as_view() , name="applied-view"),
    path('add-skill/' , SkillAddView.as_view() , name='add-skill'),
    path('add-category/' , CategoryAddView.as_view() , name='add-category'),
    path('add-department/' , AddDepartment.as_view() , name='add-category'),
    path('edit_app/<int:id>/', edit_appA, name="edit_appA"),
    path('change-status/', ChangeStatus.as_view(), name="ChangeStatus"),
    path('edit-skill/', EditSkill.as_view(), name="edit-skill"),
    path('edit-category/' , EditCategory.as_view() , name="edit-category"),
    path('edit-department/' , EditDepartment.as_view() , name="edit-department"),
    path('delete-department/' , DeleteDepartment.as_view() , name="edit-department"),
    path('delete-skill/' , DeleteSkill.as_view() , name="edit-department"),
    path('post-job/' , PostJob.as_view() , name="post-job"),
    path('req-cat/' , RequestCatAddView.as_view() , name="req-cat"),
    path('req-accept/' , AddRequestCategory.as_view() , name="req-cat"),
    path('job/' , ViewJobSingle.as_view() , name="req-cat"),
    path('update-profile/' , UpdateProfile.as_view() , name="update-profile"),
    path('view-profile/' , ViewProfile.as_view() , name="ViewProfile"),
    path('user-details/' , UserDetails.as_view() , name="user-details"),
    path('recruiter-profile/' ,RecruiterProfileDetails.as_view() , name='recruiter-profile'),
    path('all-jobs/' ,ViewAllJobs.as_view() , name='all-jobs'),
    path('apply-job/' ,ApplyJob.as_view() , name='apply-job'),
    path('filter-job/' ,JobFilerView.as_view() , name='filete-job'),
    
]

urlpatterns += router.urls