from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):
  subject= 'Welcome to instagram'
  sender = 'rehemafaith01@gmail.com'

  text_content = render_to_string('email/instaemail.txt',{"name":name})
  html_content = render_to_string('email/instaemail.html',{"name":name})

  msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
  msg.attach_altervative(html_content,'text/html')
  msg.send()