# Import Requests for POST Method
import requests

from App.Services.Notification import Notification


class SMSNotification(Notification):
    api_end_point = "https://www.sms4free.co.il/ApiSMS/SendSMS"

    def __init__(self):
        self.message = {}

    def __set_message(self, msg: dict):
        """
        SMS customization
        :param msg: message data
        :return:
        """
        self.message["key"] = msg['Key']
        self.message["user"] = msg['From']
        self.message["pass"] = msg['Password']  # sms4free.co.il account
        self.message["sender"] = msg['Subject']
        self.message["recipient"] = msg['To']

    def add_attachment(self, text: str) -> None:
        """
        set text to SMS
        :param text: SMS text
        :return:
        """
        self.message["msg"] = text

    def send_message(self) -> None:
        """
        Post Data
        :return: None
        """
        response = requests.post(self.api_end_point, json=self.message)
        print(response)  # Should GET Status 200 (SUCCESS)

    def send_notification(self) -> bool:
        """
        send SMS
        :return: None
        """
        # Define The URL We Wanna Post to

        key = "pDrHzFaep"
        user = "0527332199"
        _pass = "16454004"
        sender = "Genetic App"
        recipient = "0527332199"

        # Object that have the data we wanna POST
        data = {"key": key,
                "user": user,
                "pass": _pass,
                "sender": sender,
                "recipient": recipient,
                "msg": self.message["msg"]}

        # Post Data
        response = requests.post(self.api_end_point, json=self.message)

        print(response) #Should GET Status 200 (SUCCESS)

        if response == 200:
            return True
        else:
            return False
