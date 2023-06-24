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

#### Run Service:
I seriously doubt anyone but me wil see this so I'm gonna forget the Venv, and pip stuff.
```
./start.sh
```
This script starts the server, loads the env variables and launchesCelery in a seperate process. It kills celery when the server is stopped. I plan to ultimately useDocker and Docker compose torun this service.

#### TODO:
- Tone down the file structure. I don't need all the directories. This service is small but when I began, I thought
  it would be bigger. So Drop, `routes`, `schemas` and `config`.
- Get the Celery portion, `tasks` finalized:
  It works fine forwhat it is, and what I need. Decide if the class is worth it or just keep the function. 
- For gods sake figure out logger!! Like why the hell does it only ever halfway work!? Maybe it's got something to do with
  how the modules are loading as to why Only info works and not error, vice versa, and why I can't ever get it to consistently write to file!!   
- Build the Info Web Page.
- Make sure the error handling is up to snuff. As is I really only know about `try: except:`. 
- Containerize the app. Have been enjoying what I'm learning with Docker, and Docker Compose.
- Make the tests hard core. I currently only have one that fires requests at the endpoint.
