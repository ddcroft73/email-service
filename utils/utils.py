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
from datetime import datetime, timedelta
from time import sleep
import os

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

    response = await smtp_email.send_mail(email)   
    #sleep(3)     
    if response:
       print("sending mail...")
    else:
       return {'result': 'Something went wrong.'}   
    # back to client   
    return {'result': f"email sent @ {datetime.now()}"}   


def verify_token(credentials: HTTPAuthorizationCredentials=Depends(HTTPBearer())) -> dict:
    try:
        token = credentials.credentials
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])

        return payload
    
    except PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid token")


def create_token() -> str:
    def days_to_expire(number_days): # fix this shizzz
        current_time = datetime.now()
        future_time = current_time + timedelta(days=number_days)
        unix_timestamp = int(future_time.timestamp())
        print(f'future_time: {future_time}')
        return unix_timestamp
    
    number_of_days = 7  
    expiration_timestamp = days_to_expire(number_of_days)

    payload = {
        'username': "TesttheService",
        'exp': expiration_timestamp,
        'iss': 'your-issuer',
        'sub': 'user-12345'
    }

    secret_key = os.getenv('SECRET_KEY')
    new_token = jwt.encode(payload, secret_key, algorithm='HS256')

    return new_token
