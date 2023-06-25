
from smtplib import SMTP_SSL, SMTPException
from ssl import create_default_context
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from settings import settings
from schema import Email
#import logging
from datetime import datetime
from time import sleep
from dotenv import load_dotenv
import random

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

    def send_mail(self, email: Email) -> bool:        
        #print(f'USERNAME: {self.username}, PASSWORD: {self.password}')        
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
        sleep(random.randint(5,25))
        '''
        try:
           with SMTP_SSL(self.smtp_host, self.smtp_port, context=create_default_context()) as email_:
             email_.login(self.username, self.password)
             email_.sendmail(self.username, email.email_to, _message)
             
        except SMTPException as smtp_err:
            print('SMTP Error:', smtp_err)
            print('Error occurred attempting to send mail', exc_info=True)
            return False    
        
        except Exception as er:
           #print(er)
           print('Error occurred attepmting to send mail')
           return False               

        print(f'Email: Sent to: {email.email_to}')   
        '''    
        return True  

# By porting the output of Celery to a file, all my print statements also go to the file. I can't get the logger to
# work right to save my life, so I just 86'd it and print any errors to the celery log file.
#logging.basicConfig(filename='send-mail-ERRORS.log', level=logging.ERROR, force=True) 

smtp_email = SmtpEmail(
    settings.SMTP_SERVER, 
    settings.SMTP_PORT, 
    settings.EMAIL_LOGIN, 
    settings.EMAIL_PASSWRD
)





