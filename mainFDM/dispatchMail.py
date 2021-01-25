from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.core import mail
from django.template.loader import render_to_string


def dispatch(choice, user):

    if choice == "BI":

        subject = "Business Intelligence"
        html_message = render_to_string('streamEmails/businessIntelligence.html', {'context': 'values'})

    elif choice == "ST":

        subject = "Software Testing"
        html_message = render_to_string('streamEmails/softwareTesting.html', {'context': 'values'})

    else:
        subject = "Technical Operations"
        html_message = render_to_string('streamEmails/technicalOperations.html', {'context': 'values'})

    plain_message = strip_tags(html_message)
    to = user

    mail.send_mail(subject, plain_message, 'MyCareerPath Team <noreply@mycareerpath.co.uk>', [to], html_message=html_message)