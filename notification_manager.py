# Platforma Twilio va trimite pe numarul de telefon al utilizatorului mesaj cu datele zborului

from twilio.rest import Client

TWILIO_SID = "***************"
TWILIO_AUTH_TOKEN = "***************"
TWILIO_VIRTUAL_NUMBER = "+1234567890"
TWILIO_VERIFIED_NUMBER = "+40712345678"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)
