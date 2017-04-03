from django.core.mail import EmailMultiAlternatives
from klayvio_weather.settings import SENDGRID_API_KEY
import sendgrid
from sendgrid.helpers.mail import Email, Content, Substitution, Mail


def send_signup_email(content, subject, to_email, template_id,
                      from_email="Seed@klayvio.com"):
    mail = EmailMultiAlternatives(
        subject=subject,
        body=content,
        from_email=from_email,
        to=[to_email],
        headers={"Reply-To": "support@sendgrid.com"}
    )
    # Add template
    mail.template_id = template_id

    # Replace substitutions in sendgrid template
    # mail.substitutions = {'%username%': 'elbuo8'}
    mail.send()


def sg_send_email(subject, body, to_email, template_id, from_email="Seed@klayvio.com", **kwargs):
    sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
    from_email = Email(from_email)
    subject = subject
    to_email = Email(to_email)
    content = Content('text/html', body)
    mail = Mail(from_email, subject, to_email, content)
    sub_tuples = kwargs.get('sub_dic').items()
    for _from, _to in sub_tuples:
        mail.personalizations[0].add_substitution(Substitution(_from, _to))
    mail.set_template_id(template_id)

    response = sg.client.mail.send.post(request_body=mail.get())
    print "Email Sent %s" % str(response.status_code)
    print response
