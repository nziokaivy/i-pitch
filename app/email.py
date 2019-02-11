from flask_mail import Message
from flask import render_template
from . import mail
subject_pref = 'PITCH'
sender_email = 'nziokaivy@gmail.com'

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)