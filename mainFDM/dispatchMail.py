from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def dispatch():
    subject = 'Software Testing'
    html_message = render_to_string('streamEmails/softwareTesting.html', {'context': 'values'})
    plain_message = strip_tags(html_message)
    from_email = 'From <team4helper@gmail.com>'
    to = 'benthompsonwatson@hotmail.co.uk'

    mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)