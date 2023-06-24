
import logging
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from utils.utils import verify_token, dispatch_email
from schemas.schema import Email
from schemas.schema import MailResponse  
from datetime import datetime
from celery_app.tasks import   send_email_task
import os
router = APIRouter()

@router.post("/send-email/" , response_model=MailResponse)
def send_email(email: Email,  payload: dict=Depends(verify_token)):   
          
     #print(email)     
     #print(os.getenv("EMAIL_PASSWRD"))

     task = send_email_task.delay(email.dict())
     
     #response = await dispatch_email(email)
     response = {
          "result": f'{task.id}, Task passed to Celery'
     }
     # Instead of semding the mail, passit off to a celery task
     # and return the task id
     return JSONResponse(response)


