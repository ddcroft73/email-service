import jwt, requests, os, sys, time
from datetime import datetime, timedelta
from dotenv import load_dotenv

from fastapi.responses import JSONResponse
# import cant find the files if you start a file from inside the directory structure.
cwd = os.getcwd()
sys.path.append(cwd)

from schemas.schema import Email, Message
from test_html_template import html as verify_email_test_code
from config.settings import settings 
import asyncio, aiohttp

# An email mustbe setup like so before itis dispatched to the service. 

email = Email(
    email_to="croftdanny1973@gmail.com",
    email_from=settings.EMAIL_FOR_SENDING,
    subject="Test Email",
    message={
        "text": "This is a test Email, THe Text Plain Text Portion",
        "html": verify_email_test_code ,
    },
)
'''
email = Email(
    email_to="croftdanny1973@gmail.com",
    email_from=settings.EMAIL_FOR_SENDING,
    subject="Test Email",
    internal_note="Testing",
    message=Message(text="",html="")
)
'''
load_dotenv()

def create_token() -> str:

    def days_to_expire(number_days): # fix this shizzz
        current_time = datetime.now()
        future_time = current_time + timedelta(days=number_days)
        unix_timestamp = int(future_time.timestamp())
        print(f'future_time: {future_time}')
        return unix_timestamp
    

    number_of_days = 7  # Set the desired number of days for token expiration
    expiration_timestamp = days_to_expire(number_of_days)

    payload = {
        'username': "YOLessTestThisShizzzzz",
        'exp': expiration_timestamp,
        'iss': 'your-issuer',
        'sub': 'user-12345'
    }

    secret_key = os.getenv('SECRET_KEY')
    new_token = jwt.encode(payload, secret_key, algorithm='HS256')

    return new_token




token: str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IllPTGVzc1Rlc3RUaGlzU2hpenp6enoiLCJleHAiOjE2ODc4ODQyNzMsImlzcyI6InlvdXItaXNzdWVyIiwic3ViIjoidXNlci0xMjM0NSJ9.hCmLv9f70C00IW9MEVcwK-DloBLWqqJBWUDkI3m3sW8'

async def fetch_data(url, headers, payload):
    async with aiohttp.ClientSession() as session:
        async with session.post(url,  headers=headers, json=payload) as response:
            
            return await response.json()


async def test_email():
    url = 'http://localhost:8000/send-email/'

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    
    # Howmany can it handle?, Now This is where I think I need touse celery and that being said
    # Id expect it to stagger the requests, and not process them ubtil the one before has been processed.
    for cnt in range(0, 1):
        time.sleep(1)
        response = await fetch_data(url, headers=headers, payload=email.dict())
        print(response)
    print(f'Sent: {cnt+1} emails')

asyncio.run(test_email())



'''
def test_send_email(token):
    headers = {'Authorization': f'Bearer {token}'}
  
    response = requests.post(
        'http://localhost:8000/send-email/', 
        headers=headers, 
        json=email.to_dict()
    )
    return response.json()



#print(token)


API_response: dict = test_send_email(token)
print(API_response)

'''



