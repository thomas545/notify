from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Service(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    schedule_at = models.DateTimeField(blank=True, null=True)
    sent = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True


class NotificationService(Service):
    user = models.ForeignKey(
        UserModel, related_name="notification_service", on_delete=models.CASCADE
    )


class EmailService(Service):
    user = models.ForeignKey(
        UserModel, related_name="email_service", on_delete=models.CASCADE
    )


class SmsService(Service):
    user = models.ForeignKey(
        UserModel, related_name="sms_service", on_delete=models.CASCADE
    )
