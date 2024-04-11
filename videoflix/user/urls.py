from django.urls import path
from .views import EditUserView, RegisterView, ConfirmEmailView, LoginUserView, LogoutView

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit-user/', EditUserView.as_view(), name='edit_user'),
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm-email/<uidb64>/<token>/', ConfirmEmailView.as_view(), name='confirm_email'),
]