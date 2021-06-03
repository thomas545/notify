from rest_framework.exceptions import ValidationError
from fcm_django.models import FCMDevice
from .models import NotificationService


class Service:
    def create(self, model, user, subject, message, schedule_at):
        obj = model.objects.create(
            user=user, subject=subject, message=message, schedule_at=schedule_at
        )
        return obj

    def set_sent(self, model, pk, sent):
        return model.objects.filter(id=pk).update(sent=sent)


class Notification(Service):
    model = NotificationService

    def send(self, user, subject, message, schedule_at):
        obj = self.create(self.model, user, subject, message, schedule_at)
        if obj.schedule_at is None:
            device = FCMDevice.objects.filter(user=user)
            if not device:
                raise ValidationError("You didn't have device on FCM, please set one.")
            result = device.first().send_message(title=subject, body=message)
            if result:
                self.set_sent(self.model, obj.id, True)


class FCMInterface:
    @classmethod
    def fcm_token(cls, user, device_id, token, device_type):
        fcm_obj = FCMDevice.objects.filter(user=user)
        if fcm_obj.exists():
            fcm_obj.update(device_id=device_id, registration_id=token, type=device_type)
        else:
            fcm_obj = FCMDevice.objects.create(
                user=user, device_id=device_id, registration_id=token, type=device_type
            )
        return fcm_obj

FCM = FCMInterface()
