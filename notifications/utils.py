import os
from twilio.rest import Client


def send_sms(phone_number, subject, message):
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID", "ACe206f2a2d0f957eb436596a3da8f8b0e")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN", "463dfe20d2710682d4407c4458402727")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message, from_="+12193518246", to=phone_number
    )
    return "Sent"
