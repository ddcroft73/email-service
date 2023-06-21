### Email Micro Service

This will be a service that I use on all my web projectst to send emails. It will be used
to send plain text as well as HTML Emails. I'm going to use fastAPI to build the server, and I will also use CElery, but I dont' think I will need celery for a while. Its just something I 
think will be a good idea for scalability.

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
