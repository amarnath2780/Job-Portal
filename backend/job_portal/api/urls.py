from django.urls import path,include
from recruiter.views import ApplicationView


urlpatterns = [
    path('user/', include('accounts.urls')),
    path('app/' , ApplicationView.as_view() , name="application")
]