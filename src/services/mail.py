from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

from src.credentials import MAIL_CONFIG

conf = ConnectionConfig(
    MAIL_USERNAME=MAIL_CONFIG['username'],
    MAIL_PASSWORD=MAIL_CONFIG['password'],
    MAIL_FROM=MAIL_CONFIG['from'],
    MAIL_PORT=MAIL_CONFIG['port'],
    MAIL_SERVER=MAIL_CONFIG['server'],
    MAIL_FROM_NAME=MAIL_CONFIG['from_name'],
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True
)


def send_mail_in_background(
    background_tasks: BackgroundTasks,
    email_to: str,
    body: str
):
    message = MessageSchema(
        subject='Login Email Confirm',
        recipients=[email_to],
        body=body,
        subtype='plain'
    )
    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message)
