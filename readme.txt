Email Micro Service

This will be a service that I use on all my web projectst to send emails. It will be used
to send plain text as well as HTML Emails. I'm going to use fastAPI to build the server, and I will also use CElery, but I dont' think I will need celery for a while. Its just something I 
think will be a good idea for scalability.

Tech Stack:
fastAPI
sqlALchemy.... meh, not so sure
Celery

Purpose:
Send EMails. Thats it. It will have one endpoint (as of now) that I will define later. 

EndPoints:
/send-email/

A request model will be defined to require:

{
  email_to: "string",
  subject: "string",
  body: "string",
  type: int {0:HTML, 1:TEXT}
}
In the case of the object properties that are type int, I plan to define constants that represent the types. Example: HTML: int = 1, PLAIN_TEXT: int = 0

1. An email send request is sent to the server
2. the server gets the request and if its urgent then it will be sent then
   asyncronously.If its normal then the email is added to the task queue.
3. If its sent immiedietly then a repsonse is sent to the client saying it was sent
   If it was queued, then the response will reflect that.
4. the action will be logged to the database to keep a record of it.


service/
  -celery/
     -__init__.py  ?? Do i need an __init__.py here?
  -db/
     -__init__.py
     db.py
  -tests/
     -__init__.py
     -test_models.py      
     -test_emails.py
  -routes/
     -__init__.py
     -email.py   
  -config/
     -__init__.py
     -constants.py
     -settings.py   
  -utils/
     -__init__.py
     -utils.py
  -static/
     -index.html
  -.env
  -.gitignore      
  -readme.md
  -main.py
  -celery_worker.py 
  -celery_tasks.py  
  -start.sh
  



