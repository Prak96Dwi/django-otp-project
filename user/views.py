""" user/views.py """
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import render

from .models import CustomUser
from .serializers import CustomUserSerializer, OTPVerificationSerializer
from .otp import TOTPVerification

class CustomUserCreateAPIView(ListCreateAPIView):
    """
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OtpVerificationAPIView(APIView):
    """
    """
    serializer_class = OTPVerificationSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = OTPVerificationSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.data.get('otp')

            otp = TOTPVerification()
            valid_token = otp.verify_token(token)

            if valid_token is not None:
                response_data = {
                    'message' : "Your OTP is valid"
                }
                return Response(response_data, status=status.HTTP_200_OK)
            response_data = {
                'message' : "Your OTP is Invalid"
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
