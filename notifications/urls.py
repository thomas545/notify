from django.urls import path, include
from . import views

urlpatterns = [
    path(
        "send-notification/",
        views.SendNotificationView.as_view(),
        name="send_notification",
    ),
    path("send-email/", views.SendEmailsView.as_view(), name="send_email"),
    path("send-sms/", views.SendSMSView.as_view(), name="send_sms"),
]
