""" user/urls.py """
from django.urls import path
from . import views


urlpatterns = [
    path('user/', views.CustomUserCreateAPIView.as_view(), name='index'),
    path('verify/', views.OtpVerificationAPIView.as_view(), name='verify')
]
