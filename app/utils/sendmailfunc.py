from django.core.mail import send_mail
from django.conf import settings


def send_email(user_email):
  subject = "Welcome"
  message = "Youa are very lucky to be one of us"
  from_email=settings.EMAIL_HOST_USER
  recipient_list=[user_email]
  send_mail(subject,message,from_email,recipient_list)