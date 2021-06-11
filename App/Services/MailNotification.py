import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# mtbxqfuvywuswthq


class MailNotification:

    def __init__(self, msg: dict):
        self.message = MIMEMultipart()

        self.__set_message(msg)

    def __set_message(self, msg: dict) -> None:
        # Setup the MIME
        self.message['From'] = msg['From']
        self.message['To'] = msg['To']
        self.message['Subject'] = msg['Subject']

    def add_attachment(self, text: str) -> None:
        # The body and the attachments for the mail
        self.message.attach(MIMEText(text, 'plain'))

    def send_message(self, sender_pass: str) -> None:
        # Create SMTP session for sending the mail
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
m = MailNotification({"From": "1hotlev@gmail.com", "To": "tamir.yur@gmail.com", "Subject": "hhh"})

m.add_attachment("empty")
m.send_message('mtbxqfuvywuswthq')
