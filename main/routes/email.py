from fastapi import APIRouter, Response, status
from main.helpers.models import EmailRequestModel
from main.helpers.utils import check_email_allowed
from main.helpers.validater import Validate
from main.modules.emailer import EmailServer


router = APIRouter(
    prefix='/email'
)
email = EmailServer()

@router.post('/send')
async def emailer_handler(body:EmailRequestModel, response:Response):
    if Validate.email(body.email):
        if check_email_allowed(body.email):
            try:
                email.send(
                    to=body.email,
                    subject=body.subject,
                    body=body.body,
                    html_body=body.html,
                    sender=body.sender
                )
            except Exception as err:
                response.status_code = status.HTTP_400_BAD_REQUEST
                return {
                    "details": str(err)
                }
            return {
                "details": "Email sent successfully"
            }
        else:
            response.status_code = status.HTTP_406_NOT_ACCEPTABLE
            return {
                "details": "Email not allowed"
            }
    else:
        response.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return {
            "details": "Email ID invalid"
        }