from rest_framework import serializers
from .models import EmailService, SmsService, NotificationService


class NotificationServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationService
        exclude = ("sent",)


class EmailServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailService
        exclude = ("sent",)


class SMSServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmsService
        exclude = ("sent",)
