from rest_framework.test import APITestCase
from model_bakery import baker

from notifications.models import NotificationService, EmailService, SmsService


class NotificationServiceTestCase(APITestCase):
    def test_notification(self):
        subject = "test notify"
        notification = baker.make(NotificationService, subject=subject)
        self.assertEqual(notification.subject, subject)


class EmailServiceTestCase(APITestCase):
    def test_email(self):
        subject = "test email"
        notification = baker.make(EmailService, subject=subject)
        self.assertEqual(notification.subject, subject)


class SmsServiceTestCase(APITestCase):
    def test_sms(self):
        subject = "test sms"
        notification = baker.make(SmsService, subject=subject)
        self.assertEqual(notification.subject, subject)
