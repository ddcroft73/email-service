from pydantic import BaseModel
from typing import Optional

class Message(BaseModel):
    text: str 
    html: str 

class Email(BaseModel):
    email_to: str
    email_from: str
    subject: str
    message: Message
'''
    def to_dict(self, *args, **kwargs):
        serialized = self.dict(*args, **kwargs)
        return serialized
'''

class MailResponse(BaseModel):
    result: str