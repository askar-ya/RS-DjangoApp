from django.core.mail import EmailMessage

from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpRequest
from django.template.loader import render_to_string

from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator as token_generator


def send_email_for_verify(request: HttpRequest, user):
    current_site = get_current_site(request)
    context = {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token_generator.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http',
    }

    message = render_to_string('registration/verify_email.html', context)
    print(message)
    email = EmailMessage(
        'verify email',
        message,
        to=[user.email],
    )

    email.send()
