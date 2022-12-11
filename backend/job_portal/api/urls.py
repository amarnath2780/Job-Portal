from django.urls import path,include
from recruiter.views import ApplicationView , CompanyAddView , CompanyView , ListCompanyView ,CompanyCategoryView, ApplyedView,RecruiterProfileView
from rest_framework import routers
from accounts.views import SeekerView , RecruiterView
from superuser.views import ListSkillView , SkillAddView ,ListCompanyDepartmentView , ListCompanyCategoryView , CategoryAddView ,PendingApp,ChangeStatus , AccepetdView , RejectedView,AddDepartment
from superuser.views import edit_appA
from superuser.views import EditSkill , EditCategory, EditDepartment ,DeleteDepartment,DeleteSkill ,ViewAllReq,AddRequestCategory
from recruiter.views import PostJob , RequestCatAddView , RecruiterProfileDetails ,RequestSkillAddView ,RequestDepartmentAddView ,ShortlistSeeker
from seeker.views import ViewAllJobs , ViewJobSingle , UpdateProfile , ViewProfile , UserDetails, ApplyJob ,JobFilerView
from superuser.views import AddRequestDepartmentView , AddRequestSkillView , ViewSkillRequest , ViewDepartmentRequest ,BannerImageView
from seeker.views import SearchBarFilter 
from recruiter.views import ApplyedJobsView , JobAppliedSeekerView , PostedJobListView , AppliedJobSingleJob , DeclineJobRequestView ,RecruiterUpdateProfile
from recruiter.views import CeleryTest , ShorlistedView ,ShortlistedAll , PaymentView , ShowAllMembership



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
router.register(r'request-skill', ViewSkillRequest , basename='add-req-skill')
router.register(r'request-departments', ViewDepartmentRequest , basename='add-req-department')
router.register(r'applied-jobs', ApplyedJobsView , basename='applied-jobs-list')
router.register(r'short-jobs', ShortlistedAll , basename='applied-jobs-list')
router.register(r'all-membership', ShowAllMembership , basename='applied-jobs-list')





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
    path('updata-reqruiter-profile/' ,RecruiterUpdateProfile.as_view() , name='recruiter-profile'),
    path('all-jobs/' ,ViewAllJobs.as_view() , name='all-jobs'),
    path('apply-job/' ,ApplyJob.as_view() , name='apply-job'),
    path('filter-job/' ,JobFilerView.as_view() , name='filete-job'),
    path('search-filter/' ,SearchBarFilter.as_view() , name='filete-search'),
    path('req-skill/' , RequestSkillAddView.as_view() , name="req-skill"),
    path('req-depart/' , RequestDepartmentAddView.as_view() , name="req-skill"),
    path('accept-department/' , AddRequestDepartmentView.as_view() , name="accept-department"),
    path('accept-skill/' , AddRequestSkillView.as_view() , name="accept-skill"),
    path('shortlist/' , ShortlistSeeker.as_view() , name="short-list"),
    path('applied-job-seekers/', JobAppliedSeekerView.as_view() , name='applied-job-seekers'),
    path('jobs-recruiter-posted/',  PostedJobListView.as_view() , name='applied-job-seekers'),
    path('applied-single-job/',  AppliedJobSingleJob.as_view() , name='applied-single-job'),
    path('banner/',  BannerImageView.as_view() , name='banner-img'),
    path('decline-job-request/',  DeclineJobRequestView.as_view() , name='decline-job-request'),
    path('test/',  CeleryTest.as_view() , name='test'),
    path('shortlist-view/',  ShorlistedView.as_view() , name='shortlisted'),
    path('payment/',  PaymentView.as_view() , name='shortlisted'),
]

urlpatterns += router.urls