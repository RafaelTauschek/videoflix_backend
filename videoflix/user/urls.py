from django.urls import path
from .views import EditUserView, RegisterView, ConfirmEmailView, LoginUserView, LogoutView, ChangePasswordView, ForgotPasswordView, PasswordResetRequestView, GetUserView

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit-user/', EditUserView.as_view(), name='edit_user'),
    path('register/', RegisterView.as_view(), name='register'),
    path('get-user-data/', GetUserView.as_view(), name='get_user'),
    path('reset-password-mail/', PasswordResetRequestView.as_view(), name='reset_password_mail'),
    path('confirm-email/<uidb64>/<token>/', ConfirmEmailView.as_view(), name='confirm_email'),
    path('password-reset-confirm/<uidb64>/<token>/', ForgotPasswordView.as_view(), name='password_reset_confirm'),
]


