from fastapi import ( 
    Depends, 
    HTTPException, 
    status
)
from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials
)
import jwt
from jwt.exceptions import PyJWTError

from schemas.schema import Email
from config.settings import settings
from utils.smtp_email import smtp_email

import logging
from datetime import datetime
from time import sleep
import asyncio
'''
def init_logger():
    logging.basicConfig(
        filename='email-sent.log', 
        level=logging.INFO, 
        format='%(asctime)s %(levelname)s: %(message)s', 
        datefmt='%Y-%m-%d %H:%M:%S'
    )
'''
async def dispatch_email(email: Email) -> dict:
    # For now just send the email.... 
    # This is where I'll passit on to celery....
    
    # send_mail.delay(email)
    # return {'result': "Email passed over to celery, consider it done, 200"}

    response = await smtp_email.send_mail(email)   
    #sleep(3)     
    if response:
       print("sending mail...")
    else:
       return {'result': 'Something went wrong. retrying in 10 seconds'}
    
    # back to client   
    return {'result': f"email sent @ {datetime.now()}"}   


def verify_token(credentials: HTTPAuthorizationCredentials=Depends(HTTPBearer())) -> dict:
    try:
        token = credentials.credentials
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])

        return payload
    
    except PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid token")
