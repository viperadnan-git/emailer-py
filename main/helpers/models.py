from pydantic import BaseModel

class EmailRequestModel(BaseModel):
    email: str
    body: str
    subject: str = None
    html: str = None
    sender: str = None