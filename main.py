from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from utils.utils import verify_token, dispatch_email
from schema import Email
from schema import MailResponse  
from celery_app.tasks import  send_email_task

app = FastAPI()

static_directory: str ="static"
app.mount("/static", StaticFiles(directory=static_directory), name="static")



@app.get('/', response_class=RedirectResponse)  #  response_class=RedirectResponse, include_in_schema=False
async def index():
    return RedirectResponse(url='/static/index.html')

@app.post("/send-email/" , response_model=MailResponse)
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

  