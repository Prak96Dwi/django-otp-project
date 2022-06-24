""" user/serializers.py """
from rest_framework import serializers
from .models import CustomUser


# class UserSerializer(serializers.Serializer):
#     """
#     This serializer class serialize the email or otp whatever the user
#     enter in the form.

#     """
#     email = serializers.EmailField(null=True)


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for user registeration

    """
    class Meta:
        """CustomUserSerializer meta class"""
        model = CustomUser
        fields = ['email']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        import pdb; pdb.set_trace()
        return CustomUser.objects.create(**validated_data)


class OTPVerificationSerializer(serializers.Serializer):
    """
    This serializes the otp of the user
    """
    otp = serializers.CharField()
