""" Manage user notifications

<Long description>
Created: <15/10/21>
"""
from App.Controllers.SettingsController import SettingsController
from App.Services.MailNotification import MailNotification
from App.Services.SMSNotification import SMSNotification


class UserNotificator:

    @staticmethod
    def send_notification(message: str, user_email: str):
        if UserNotificator.__is_sms_notification_on():
            UserNotificator.__send_sms_notification(message)

        if UserNotificator.__is_email_notification_on():
            UserNotificator.__send_email_notification(user_email, message)

    @staticmethod
    def __send_sms_notification(message: str) -> bool:
        is_sms_send: bool

        sms = SMSNotification()
        sms.add_attachment(message)
        is_sms_send = sms.send_notification()
        return is_sms_send

    @staticmethod
    def __send_email_notification(email: str, message_text: str) -> None:
        """
        call to MailNotification to purpose send message
        :return: return None
        """
        message: dict = {'From': "1hotlev@gmail.com",
                         'To': email,
                         'Subject': "Genetic App"}

        email = MailNotification(message)
        email.add_attachment(message_text)
        email.send_message('szojpvlaoewaoeyr')

    @staticmethod
    def __is_sms_notification_on() -> bool:
        """
        check if in settings enabled to send SMS notifications.
        :return: True if enabled otherwise False.
        """
        return SettingsController().get_sms_notification_status() == "True"

    @staticmethod
    def __is_email_notification_on() -> bool:
        """
        call to SettingsController and check email notification status is enabled.
        :return: True if notification status enabled otherwise False.
        """
        return SettingsController().get_email_notification_status() == "True"
