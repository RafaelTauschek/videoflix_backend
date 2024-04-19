from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import CustomUserSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.http import HttpResponseRedirect
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from .emails import send_confirmation_email, send_password_reset_email
from django.contrib.auth import authenticate
from django.contrib.auth import update_session_auth_hash


class ConfirmEmailView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = get_user_model().objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            return Response({"message": "Ungültiger Bestätigungslink oder abgelaufen."}, status=400)

        if user is not None and default_token_generator.check_token(user, token):
            user.valid = True
            user.save()
            return HttpResponseRedirect("http://localhost:5173/")
        else:
            return Response({"message": "Ungültiger Bestätigungslink oder abgelaufen."}, status=400)


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_confirmation_email(user, request)
            return Response({"message": "Benutzer erfolgreich erstellt."}, status=201)
        else:
            return Response(serializer.errors, status=400)

class LoginUserView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)
        if user is None:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
        elif not user.valid:
            return Response({'error': 'Not Validated'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            token, created = Token.objects.get_or_create(user=user)
            user.status = True
            user.save()
            return Response({'token': token.key})  

class EditUserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        user = request.user
        serializer = CustomUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Benutzerdaten aktualisiert."})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    def patch(self, request, *args, **kwargs):
        user = request.user
        serializer = CustomUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Benutzerdaten aktualisiert."})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class ChangePasswordView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        current_password = request.data.get('current_password')
        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')

        if new_password != confirm_password:
            return Response({"error": "Die neuen Passwörter stimmen nicht überein."}, status=status.HTTP_400_BAD_REQUEST)

        if not user.check_password(current_password):
            return Response({"error": "Das aktuelle Passwort ist falsch."}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()
        return Response({"message": "Passwort erfolgreich geändert."})
    

class PasswordResetRequestView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        if email:
            user = get_user_model().objects.filter(email=email).first()
            if user:
                send_password_reset_email(user, request)
                return Response({"message": "Eine E-Mail zum Zurücksetzen des Passworts wurde gesendet."}, status=200)
            else:
                return Response({"error": "Kein Benutzer mit dieser E-Mail gefunden."}, status=404)
        else:
            return Response({"error": "E-Mail-Adresse ist erforderlich."}, status=400)
    
    
class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        request.user.status = False
        request.user.save()
        return Response(status=204)