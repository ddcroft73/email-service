
import logging
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from utils.utils import verify_token, dispatch_email
from schemas.schema import Email
from schemas.schema import MailResponse  
from datetime import datetime

router = APIRouter()

@router.post("/send-email/" , response_model=MailResponse)
async def send_email(email: Email,  payload: dict=Depends(verify_token)):   

     response = await dispatch_email(email)
     
     # Instead of semding the mail, passit off to a celery task
     # and return the task id
     return JSONResponse(response)
      