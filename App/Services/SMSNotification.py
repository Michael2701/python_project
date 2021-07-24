# Import Requests for POST Method
import requests
import Notification


class SMSNotification(Notification):
    api_end_point = "https://www.sms4free.co.il/ApiSMS/SendSMS"

    def __init__(self):
        self.message = {}


    def __set_message(self, msg: dict):
        self.message["key"] = msg['Key']
        self.message["user"] = msg['From']
        self.message["pass"] = msg['Password']  # sms4free.co.il account
        self.message["sender"] = msg['Subject']
        self.message["recipient"] = msg['To']

    def add_attachment(self, text: str) -> None:
        self.message["msg"] = text

    def send_message(self):
        # Post Data
        response = requests.post(self.api_end_point, json=self.message)
        print(response)  # Should GET Status 200 (SUCCESS)

    def send_notification(self):
        # Define The URL We Wanna Post to


        key = "pDrHzFaep"
        user = "0527332199"
        _pass = "16454004"
        sender = "Test"
        recipient = "0527332199"
        msg = "Testing Api Using Python"

        # Object that have the data we wanna POST
        data = {}

        data["key"] = key
        data["user"] = user
        data["pass"] = _pass
        data["sender"] = sender
        data["recipient"] = recipient
        data["msg"] = msg

        # Post Data
        response = requests.post(self.api_end_point, json=self.message)

        print(response) #Should GET Status 200 (SUCCESS)