from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import (
    NotificationServiceSerializer,
    EmailServiceSerializer,
    SMSServiceSerializer,
)
from .models import EmailService, SmsService, NotificationService
from .tasks import send_emails_without_schedule, send_sms_without_schedule
from .interfaces import Notification

UserModel = get_user_model()


class SendNotificationView(generics.CreateAPIView):
    serializer_class = NotificationServiceSerializer
    queryset = NotificationService.objects.all()

    def perform_create(self, serializer):
        serializer.save()
        if not serializer.validated_data.get("schedule_at", None):
            user = serializer.validated_data.get("user")
            Notification().send(
                user,
                serializer.validated_data.get("subject", ""),
                serializer.validated_data.get("message", ""),
                serializer.validated_data.get("schedule_at", None),
            )


class SendEmailsView(generics.CreateAPIView):
    serializer_class = EmailServiceSerializer
    queryset = EmailService.objects.all()

    def perform_create(self, serializer):
        serializer.save()
        if not serializer.validated_data.get("schedule_at", None):
            user = serializer.validated_data.get("user")
            send_emails_without_schedule.delay(
                serializer.validated_data.get("subject", ""),
                serializer.validated_data.get("message", ""),
                [user.email],
                serializer.validated_data.get("pk", ""),
            )


class SendSMSView(generics.CreateAPIView):
    serializer_class = SMSServiceSerializer
    queryset = SmsService.objects.all()

    def perform_create(self, serializer):
        serializer.save()
        if not serializer.validated_data.get("schedule_at", None):
            user = serializer.validated_data.get("user")
            send_sms_without_schedule.delay(
                serializer.validated_data.get("pk", ""),
                user.phone_number,
                serializer.validated_data.get("subject", ""),
                serializer.validated_data.get("message", ""),
            )
