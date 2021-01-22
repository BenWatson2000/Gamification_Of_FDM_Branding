from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def dispatch(choice,user):

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
    from_email = 'MyCareerPath'
    to = user

    mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)