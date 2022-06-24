""" user/signals.py """
from django_otp.oath import totp

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail

from .models import CustomUser
from .otp import TOTPVerification


@receiver(post_save, sender=CustomUser)
def create_customUser(sender, instance, created, **kwargs):
    if created:
        # send otp to the user
        otp = TOTPVerification(instance)
        required_token = otp.generate_token()

        subject = 'welcome to GFG world'
        
        message = f"""
        Hi {instance.email}, thank you for registering in geeksforgeeks.
        {required_token} is your One Time Password.
        """
        
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [instance.email, ]
        send_mail(subject, message, email_from, recipient_list)
