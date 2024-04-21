from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
import base64
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.conf import settings

def safe_url_base64_encode(data):
    return base64.urlsafe_b64encode(data).decode('utf-8')

def send_confirmation_email(user, request):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    confirmation_link = request.build_absolute_uri(
        reverse('confirm_email', kwargs={'uidb64': uid, 'token': token})
    )
    additional_info = "Bitte bestätigen Sie Ihre E-Mail-Adresse, um Ihre Registrierung abzuschließen."
    subject = 'Bitte bestätigen Sie Ihre E-Mail-Adresse'
    message = (
    f'Hallo!\n\n'
    f'Dein Bestätigungslink: {confirmation_link}\n\n'
    f'{additional_info}\n\n'
    'Vielen Dank!'
)
    send_mail(subject, message, 'from@example.com', [user.email])
    
    
    
def send_password_reset_email(user, request):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    
    password_reset_link = f'{settings.FRONTEND_URL}/forgot-password-reset/{uid}/{token}/'

    subject = 'Passwort zurücksetzen'
    message = (
    f'Hallo!\n\n'
    f'Bitte verwende den folgenden Link, um dein Passwort zurückzusetzen: {password_reset_link}\n\n'
    'Vielen Dank!')
    send_mail(subject, message, 'from@example.com', [user.email])
    
    
    