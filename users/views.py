from django.shortcuts import render
from rest_framework.exceptions import NotAcceptable
from dj_rest_auth.views import LoginView
from notifications.interfaces import FCM


class UserLoginView(LoginView):
    def post(self, request, *args, **kwargs):
        response = super(UserLoginView, self).post(request, *args, **kwargs)
        notification_token = request.data.get("notification_token", None)
        device_id = request.data.get("device_id", None)
        device_type = request.data.get("device_type", None)
        if not notification_token or not device_type:
            raise NotAcceptable("notification token and device_type are required")
        FCM.fcm_token(self.user, device_id, notification_token, device_type)
        return response
