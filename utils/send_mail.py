from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from config import settings


def send_mail(receipient, subject, plain_text_content):
    """_summary_
        Takes in receipient, subject, and plain_text_content as arguments.
    """
    mail_obj = Mail(
        from_email=settings.DEFAULT_FROM_EMAIL,
        to_emails=receipient,
        subject=subject,
        plain_text_content=plain_text_content,
    )
    
    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(mail_obj)
        print(response.status_code)
        
    except Exception as e:
        print(str(e))