from celery_app.celery import app
from schema import Email, Message
from utils.smtp_email import smtp_email
from celery import Task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

logger.info("started...")

# Experimenting with This setup... it may be more troublethan its worth.. lol
class EmailTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        pass

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        logger.error(f"Failed to send email: {exc}")



@app.task(base=EmailTask, bind=True, max_retries=3, default_retry_delay=10)
def send_email_task(self, email_dict: dict[str, str]):
    def on_retry(exc): 
        pass

    def on_timeout(soft, timeout):
        logger.error("Email task timed out")

    try:
        email = Email(**email_dict)
        response = smtp_email.send_mail(email)
        return response
    
    except Exception as exc:
        raise self.retry(exc=exc, hook=on_retry)

    self.request.on_timeout = on_timeout