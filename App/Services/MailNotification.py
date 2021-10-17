""" This class help notify user by Email about some event. """

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MailNotification:

    def __init__(self, msg: dict):
        """
        :param msg: text of message
        """
        self.message = MIMEMultipart()
        self.__set_message(msg)

    def __set_message(self, msg: dict) -> None:
        """
        Setup the MIME
        :param msg: text of message
        :return: None
        """
        self.message['From'] = msg['From']
        self.message['To'] = msg['To']
        self.message['Subject'] = msg['Subject']

    def add_attachment(self, text: str) -> None:
        """
        The body and the attachments for the mail
        :param text: MIMEText attachment
        :return:
        """
        self.message.attach(MIMEText(text, 'plain'))

    def send_message(self, sender_pass: str) -> None:
        """
        Create SMTP session for sending the mail
        :param sender_pass:
        :return:
        """
        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port

        try:
            session.starttls()  # enable security
            session.login(self.message['From'], sender_pass)  # login with mail_id and password

            text = self.message.as_string()
            session.sendmail(self.message['From'], self.message['To'], text)
            print('Mail Sent')
        except Exception as e:
            print(e)
        finally:
            session.quit()


# Test
# m = MailNotification({"From": "1hotlev@gmail.com", "To": "tamir.yur@gmail.com", "Subject": "Subject Mail"})
# m.add_attachment("empty")
# m.send_message('szojpvlaoewaoeyr')
