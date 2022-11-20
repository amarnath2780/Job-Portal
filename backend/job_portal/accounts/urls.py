from django.urls import path, include
from . import views



urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('verify-otp/',views.Verify_otpView.as_view(), name='verify-otp'),
    path('login/', views.LoginView.as_view(), name='user_login'),
    path('detail/<str:pk>/', views.UserView.as_view(), name='user_detail'),
]

