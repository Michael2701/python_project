""" Manage user notifications

<Long description>
Created: <15/10/21>
"""
from App.Controllers.SettingsController import SettingsController
from App.Services.MailNotification import MailNotification
from App.Services.SMSNotification import SMSNotification


class UserNotificator:

    def __init__(self, message: str):
        if self.is_sms_notification_on():
            print("is_sms_notification_on = true")
            print(self.send_sms_notification(message))

        if self.is_email_notification_on():
            self.send_email_notification(message)

    def send_sms_notification(self, message: str) -> bool:
        is_sms_send: bool

        sms = SMSNotification()
        sms.add_attachment("Hi, calculation completed")
        is_sms_send = sms.send_notification()
        return is_sms_send

    def send_email_notification(self, message: str) -> None:
        message: dict = {'From': "1hotlev@gmail.com",
                         'To': "a", # TODO add recipient
                         'Subject': "Genetic App - Calculation Completed"}

        email = MailNotification(message)
        email.add_attachment('Hi, Calculation Completed')
        email.send_message('szojpvlaoewaoeyr')

    def is_sms_notification_on(self) -> bool:
        """

        :return:
        """
        return SettingsController().get_sms_notification_status() == "True"

    def is_email_notification_on(self) -> bool:
        """

        :return:
        """
        return SettingsController().get_email_notification_status() == "True"


UserNotificator("Default message")
