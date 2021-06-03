from django.contrib import admin
from .models import NotificationService, EmailService, SmsService


admin.site.register(NotificationService)
admin.site.register(EmailService)
admin.site.register(SmsService)
