import logging
from smtplib import SMTP, SMTPServerDisconnected
from main import config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from types import SimpleNamespace


log = logging.getLogger(__name__)


class EmailServer:
    def __init__(self) -> None:
        self.__config = SimpleNamespace(**config.smtp)
        self.__server = self.connect()

    def connect(self):
        log.info('Starting SMTP client...')
        self.__server = SMTP(
            host=self.__config.host, port=self.__config.port)
        self.__server.ehlo()
        log.info('Putting the connection into TLS mode...')
        self.__server.starttls()
        log.info('Logging into SMTP server...')
        self.__server.login(
            user=self.__config.username,
            password=self.__config.password
        )
        log.info('SMTP logging successful')
        return self.__server


    def create_email_body(self, body: str, html_body):
        log.info('Creating E-mail Body...')
        email_body = MIMEMultipart('alternative')
        plain_part = MIMEText(body, 'plain')
        email_body.attach(plain_part)
        if html_body:
            html_part = MIMEText(html_body, 'html')
            email_body.attach(html_part)
        return email_body

    def send_email(self, sender:str, to:str, body:str):
        log.info('Sending E-mail to {to}'.format(to=to))
        try:
            self.__server.sendmail(from_addr=sender, to_addrs=to, msg=body)
        except SMTPServerDisconnected:
            self.connect()
            self.send_email(sender=sender, to=to, body=body)


    def send(self, to: str, subject: str, body: str, html_body=None, sender: str = None):
        email_body = self.create_email_body(body=body, html_body=html_body)
        if not sender:
            sender = self.__config.username
        email_body['From'] = sender
        email_body['To'] = to
        if subject:
            email_body['Subject'] = subject
        self.send_email(sender, to, email_body.as_string())