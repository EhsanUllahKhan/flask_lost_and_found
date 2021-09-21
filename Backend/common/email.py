"""Send email"""

from flask_mail import Message
from flask import current_app
from config import config
from Backend.common.celery_app import celery

from Backend.Models.Email_model import Email as EmailModel
# import app
from Backend import mail
import yagmail


@celery.task(name="send_email")
def send_email(to, subject):
    """Send email"""
    app = current_app
    recipients = [to]
    msg = Message(subject, recipients=recipients, sender=config.MAIL_DEFAULT_SENDER)
    with app.app_context():
        mail.send(msg)

@celery.task(name="send_email_yagmail")
def send_emai_yagmail(to, subject, content):
    MAIL_ID = config.MAIL_USERNAME
    MAIL_PASSWORD = config.MAIL_PASSWORD
    yag = yagmail.SMTP(MAIL_ID, MAIL_PASSWORD)
    yag.send(
        to=to,
        subject=subject,
        contents=content
    )


@celery.task(name="send_email_with_attachment_yagmail")
def send_with_attachment(to, subject, content, attachment):
    MAIL_ID = config.MAIL_USERNAME
    MAIL_PASSWORD = config.MAIL_PASSWORD
    yag = yagmail.SMTP(MAIL_ID, MAIL_PASSWORD)
    yag.send(
        to=to,
        subject=subject,
        contents=content,
        attachments=attachment,
    )