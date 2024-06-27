from django.core.mail import send_mail
from confs.settings import EMAIL_HOST_USER

def send_msg(title: str, message: str, receiver: str):
    send_mail(title, message, EMAIL_HOST_USER, [receiver])