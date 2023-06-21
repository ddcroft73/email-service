## Email Micro Service

This will be a service that I use on all my web projectst to send emails. It will be used
to send plain text as well as HTML Emails. I'm going to use fastAPI to build the server, and I will also use CElery, but I dont' think I will need celery for a while. Its just something I 
think will be a good idea for scalability.

### Tech Stack:
fastAPI
Celery

### Purpose:
Send EMails. Thats it. It will have one endpoint (as of now) that I will define later. 

### EndPoint:
/send-email/

A request model will be defined to require:

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
### Response Model:

```
{
  "result": "string"
}
```
### Workflow

1. An email send request is sent to the server
2. The server verifies the clients credentials
3. the email is passed to Celery
4. A response is sent back to the client.
5. THe email is sent FIFO.

There is error handling (still beefing it up), and the Celery part is still WIP.. Its all WIP.
