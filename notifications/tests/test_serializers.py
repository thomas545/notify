from rest_framework.test import APITestCase
from model_bakery import baker

from notifications.models import NotificationService, EmailService, SmsService
from notifications.serializers import (
    NotificationServiceSerializer,
    EmailServiceSerializer,
    SMSServiceSerializer,
)


class ServiceTestCase(APITestCase):
    def setUp(self):
        self.user = baker.make("users.User")


class NotificationServiceTestCase(ServiceTestCase):
    def test_create_notification_serializer(self):
        data = {
            "subject": "notification 1",
            "message": "Hello World, notification",
            "schedule_at": None,
            "user": self.user.pk,
        }
        serializer = NotificationServiceSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        self.assertEqual(serializer.data.get("message"), data.get("message"))

    def test_get_notification_serializer(self):
        notification = baker.make(NotificationService)
        serializer = NotificationServiceSerializer(instance=notification)

        self.assertEqual(serializer.data.get("message"), notification.message)


class EmailServiceTestCase(ServiceTestCase):
    def test_create_email_serializer(self):
        data = {
            "subject": "Email 1",
            "message": "Hello World, email",
            "schedule_at": None,
            "user": self.user.pk,
        }
        serializer = EmailServiceSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        self.assertEqual(serializer.data.get("message"), data.get("message"))

    def test_get_email_serializer(self):
        email = baker.make(EmailService)
        serializer = EmailServiceSerializer(instance=email)

        self.assertEqual(serializer.data.get("message"), email.message)


class SMSServiceTestCase(ServiceTestCase):
    def test_create_sms_serializer(self):
        data = {
            "subject": "sms 1",
            "message": "Hello World, sms",
            "schedule_at": None,
            "user": self.user.pk,
        }
        serializer = SMSServiceSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        self.assertEqual(serializer.data.get("message"), data.get("message"))

    def test_get_sms_serializer(self):
        sms = baker.make(SmsService)
        serializer = SMSServiceSerializer(instance=sms)

        self.assertEqual(serializer.data.get("message"), sms.message)
