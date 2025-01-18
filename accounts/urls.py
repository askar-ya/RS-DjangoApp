from django.urls import path
from django.views.generic import TemplateView

from .views import Registration, VerifyEmail, MyLoginView, Profile


urlpatterns = [
    path('profile/', Profile.as_view(), name='profile'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('signup/', Registration.as_view(), name='Регистрация'),
    path('confirm_email/', TemplateView.as_view(template_name='registration/confirm_email.html'),
         name='confirm_email'),
    path('verify_email/<uidb64>/<token>/', VerifyEmail.as_view(), name='verify_email'),
    path('invalid_verify/', TemplateView.as_view(template_name='registration/invalid_verify.html')
         , name='invalid_verify'),
]
