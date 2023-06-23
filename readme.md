### Email Micro Service

This will be a service that I use on all my web projectst to send emails. It will be used
to send plain text as well as HTML Emails. The main purpose will be verify Email emails, reset password emails, and anything pertaining to the apps core function. I'm going to use fastAPI to build the server, and I will also use CElery.

#### Tech Stack:
fastAPI<br>
Celery

#### Purpose:
Send EMails. Thats it. It will have one endpoint (as of now) that I will define later. 

#### EndPoint:
/send-email/

#### Request Model:

```
{
  email_to: "string",
  email_from: "string",
  subject: "string",
  message: {
    text: "string",
    html: "string
  }
}
```
#### Response Model:

```
{
  "result": "string"
}
```
#### Workflow

1. A request is sent to the server with all it needs to be mailed.
2. The server verifies the clients credentials via dependencies.
3. The request is passed to Celery, with all the relevent data.
4. A response is sent back to the client.
5. The email is sent FIFO.

There is error handling (still beefing it up), and the Celery part is still WIP.. Its all WIP.

#### Run Service:
```
./start.sh
```
This script starts the server, loads the env variables and launchesCelery in a seperate process. It kills celery when the server is stopped. I plan to ultimately useDocker and Docker compose torun this service.

#### TODO:
1. Build the Info Web Page.
2. Make sure the error handling is up to snuff. As is I really only know about `try: except:`. 
3. Look into Docker... yeh... do I still need a venv? I'm not even sure.
4. Make the tests hard core. I currently only have one that fires requests at the endpoint.
