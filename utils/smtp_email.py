
from smtplib import SMTP_SSL, SMTPException
from ssl import create_default_context
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config.settings import settings
from schemas.schema import Email
import logging
from datetime import datetime
from time import sleep


class SmtpEmail():
    def __init__(self, smtp_host: str, smtp_port: int, username: str, password: str):
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
        
    def prepare_message(
            self, 
            em_from: str, 
            em_to: str, 
            sub: str, 
            html: str, 
            text: str
    ) -> str:
        message = MIMEMultipart("alternative")
        message["Subject"] = sub
        message["From"] = em_from
        message["To"] = em_to
        
        txt_part = MIMEText(text, "plain")
        html_part = MIMEText(html, "html")

        message.attach(txt_part)
        if not html == "":
             message.attach(html_part)

        return message.as_string()

    async def send_mail(self, email: Email) -> bool:
        
        html = email.message.html if email.message.html != "" else ""
        text = email.message.text if email.message.text != "" else ""

        _message = self.prepare_message(
           email.email_from, 
           email.email_to, 
           email.subject, 
           html, 
           text
        ) 
        # simulate sending email.. so I dont wreck it.
        sleep(1.5)
        ''' 
        try:
           with SMTP_SSL(self.smtp_host, self.smtp_port, context=create_default_context()) as email:
             email.login(self.username, self.password)
             email.sendmail(self.username, email_message.email_to, _message)
             
        except SMTPException as smtp_err:
            print(er)
            logging.error('SMTP Error:', smtp_err)
            logging.error('Error occurred attempting to send mail', exc_info=True)
            return False    
        
        except Exception as er:
           print(er)
           logging.error('Error occurred attepmting to send mail')
           return False               
           '''
        return True 


 

logging.basicConfig(filename='send-mail-ERRORS.log', level=logging.ERROR, force=True) 

smtp_email = SmtpEmail(
    settings.SMTP_SERVER, 
    settings.SMTP_PORT, 
    settings.EMAIL_LOGIN, 
    settings.EMAIL_PASSWRD
)





