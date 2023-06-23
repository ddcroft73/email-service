from celery_app.celery import app
from schemas.schema import Email, Message
from utils.smtp_email import smtp_email
from celery import Task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

# instead of a function define a class here with error handling.
@app.task(bind=True)
def send_email_task(self, email_dict: dict[str, str]):
    email = Email(**email_dict)    
    response = smtp_email.send_mail(email)
    return response

'''
WIP Thinking a class will give me more control.. not quite right yet.
@app.task(bind=True, max_retries=3, default_retry_delay=10)
class EmailTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        # This method is called when the task succeeds
        logger.info("Email sent successfully!")
        # You can add additional logic here if needed

    def on_failure(self, exc: Exception, task_id, args, kwargs, einfo):
        # This method is called when the task fails
        logger.error(f"Failed to send email: {exc}")
        # You can add additional error handling or logging here

    def send_email(self, email_dict):
        try:
            email = Email(**email_dict)    
            response = smtp_email.send_mail(email)
            return response

        except Exception as exc:
            # Raise an exception to trigger the on_failure method and retry if necessary
            raise self.retry(exc=exc)

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        # This method is called when the task is retried
        logger.warning(f"Retrying email task: {exc}")
        # You can add additional retry-related handling or logging here

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        # This method is called after the task has finished (regardless of success or failure)
        logger.info("Email task completed")
        # You can perform any cleanup or final actions here

    def on_timeout(self, soft, timeout):
        # This method is called when the task exceeds its time limit (soft or hard timeout)
        logger.error("Email task timed out")
        # You can handle the timeout scenario or perform necessary actions here

email_task = EmailTask()

'''