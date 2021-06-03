from notifications.models import EmailService, SmsService
from django.utils import timezone
from django.core.mail import send_mail
from celery import shared_task
from .interfaces import Service
from .utils import send_sms


@shared_task(bind=True, max_retries=5)
def send_sms_without_schedule(self, sms_id, phone_number, subject, message):
    try:
        send_sms(phone_number, subject, message)
        Service().set_sent(SmsService, sms_id, timezone.now())
        return f"SMS to {phone_number} was sent."
    except Exception as exc:
        print(f"{phone_number} failed to send.")
        self.retry(exc=exc, countdown=600)


@shared_task(bind=True, max_retries=5)
def send_emails_without_schedule(self, subject, message, recipient_list, obj_id):
    try:
        send_mail(subject, message, recipient_list=recipient_list, fail_silently=False)
        Service().set_sent(EmailService, obj_id, timezone.now())
        return f"Email to {recipient_list} was sent."
    except Exception as exc:
        print(f"{recipient_list} failed to send.")
        self.retry(exc=exc, countdown=600)


@shared_task
def send_sms_with_schedule():
    all_sms = SmsService.objects.filter(
        sent__isnull=True, schedule_at__lte=timezone.now()
    ).only("user", "subject", "message").select_related("user")
    for sms in all_sms:
        send_sms(sms.user.phone_number, sms.subject, sms.message)
        Service().set_sent(EmailService, sms.id, timezone.now())


@shared_task
def send_emails_with_schedule():
    emails = EmailService.objects.filter(
        sent__isnull=True, schedule_at__lte=timezone.now()
    ).only("user", "subject", "message").select_related("user")
    for email in emails:
        send_mail(
            email.subject,
            email.message,
            recipient_list=[email.user.email],
            fail_silently=False,
        )
        Service().set_sent(EmailService, email.id, timezone.now())
