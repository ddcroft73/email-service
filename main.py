from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from utils.utils import verify_token, dispatch_email
from schema import Email
from schema import MailResponse  
from celery_app.tasks import  send_email_task

app = FastAPI()


app.mount("/static", StaticFiles(directory='static'), name="static")
@app.get('/', response_class=RedirectResponse)  
async def index():
    return RedirectResponse(url='/static/index.html')

@app.post("/send-email/" , response_model=MailResponse)
def send_email(email: Email,  payload: dict=Depends(verify_token)):   
          
     task = send_email_task.delay(email.dict())     
     #response = await dispatch_email(email) #without Celery. it still works just add async \await down the chain. 
     response = {
          "result": f'{task.id}, Task passed to Celery'
     }
     return JSONResponse(response)

  