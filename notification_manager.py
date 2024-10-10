from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client("[YOUR USERNAME FROM TWILIO]","[YOUR PASSWORD FROM TWILIO]")

    def send_whatsapp(self,message_body):
        message = self.client.messages.create(from_=f"whatsapp:[YOUR TWILIO.NO]",
            body=message_body,to=f"whatsapp:[YOUR TWILIO VERIFIED NUMBER]")
        print(message.sid)