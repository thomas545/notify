from django.urls import reverse
from rest_framework.test import APITestCase
from model_bakery import baker

from notifications.models import NotificationService, EmailService, SmsService
from notifications.serializers import (
    NotificationServiceSerializer,
    EmailServiceSerializer,
    SMSServiceSerializer,
)
from notifications.interfaces import FCM


class ServiceTestCase(APITestCase):
    def setUp(self):
        self.user = baker.make("users.User")
        self.data = {
            "subject": "notification",
            "message": "Hello World",
            "schedule_at": None,
            "user": self.user.pk,
        }


class NotificationTestCase(ServiceTestCase):
    def test_send_notification_without_device(self):
        url = reverse("send_notification")
        response = self.client.post(url, data=self.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json()[0], "You didn't have device on FCM, please set one."
        )

    def test_send_notification_with_device(self):
        url = reverse("send_notification")
        fcm = FCM.fcm_token(self.user, "123", "123", "ios")
        response = self.client.post(url, data=self.data)
        print(response.json())
        self.assertEqual(response.status_code, 201)


class EmailTestCase(ServiceTestCase):
    def test_send_email_view(self):
        url = reverse("send_email")
        response = self.client.post(url, data=self.data)
        self.assertEqual(response.status_code, 201)


class SMSTestCase(ServiceTestCase):
    def test_send_sms_view(self):
        url = reverse("send_sms")
        response = self.client.post(url, data=self.data)
        self.assertEqual(response.status_code, 201)
