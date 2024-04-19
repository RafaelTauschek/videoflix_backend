from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse

def send_confirmation_email(user, request):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    user_name = user.username
    confirmation_link = request.build_absolute_uri(
        reverse('confirm_email', kwargs={'uidb64': uid, 'token': token})
    )
    additional_info = "Bitte bestätigen Sie Ihre E-Mail-Adresse, um Ihre Registrierung abzuschließen."
    subject = 'Bitte bestätigen Sie Ihre E-Mail-Adresse'
    message = (
    f'Hallo {user_name},\n\n'
    f'Ihr Bestätigungslink: {confirmation_link}\n\n'
    f'{additional_info}\n\n'
    'Vielen Dank!'
)
    send_mail(subject, message, 'from@example.com', [user.email])
    
    
    
def send_password_reset_email(user, request):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    password_reset_link = request.build_absolute_uri(
        reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
    )

    subject = 'Passwort zurücksetzen'
    message = f'Bitte verwenden Sie den folgenden Link, um Ihr Passwort zurückzusetzen: {password_reset_link}'
    send_mail(subject, message, 'from@example.com', [user.email])