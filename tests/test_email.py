import os, sys, time, requests
from dotenv import load_dotenv

from fastapi.responses import JSONResponse
# import cant find the files if you start a file from inside the directory structure.
cwd = os.getcwd()
sys.path.append(cwd)

from schema import Email, Message
from utils.utils import create_token
from test_html_template import html as verify_email_test_code
from settings import settings 
import asyncio, aiohttp

# An email mustbe setup like so before itis dispatched to the service. 

email = Email(
    email_to="croftdanny1973@gmail.com",
    email_from=settings.EMAIL_FOR_SENDING,
    subject="Test Email",
    message=Message(
        text="This is a test Email, THe Text Plain Text Portion",
        html=verify_email_test_code
    )    
)

load_dotenv()


async def fetch_data(url, headers, payload):
    async with aiohttp.ClientSession() as session:
        async with session.post(url,  headers=headers, json=payload) as response:            
            return await response.json()

def test_email(token):
    url = 'http://localhost:8000/send-email/'

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    '''
    for cnt in range(0, 1):
        time.sleep(1)
        response = await fetch_data(url, headers=headers, payload=email.dict())
        print(response)
        
    print(f'Sent: {cnt+1} emails')
    '''

    # Use this to send requests back to back, usually set to only one.
    for _ in range(1):
        time.sleep(1)
        response = requests.request("POST", url, headers=headers, json=email.dict())
        print(response.json())

token:  str = create_token()

#asyncio.run(test_email(token))
test_email(token)