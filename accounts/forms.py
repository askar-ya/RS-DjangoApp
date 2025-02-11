from django.contrib.auth import get_user_model, authenticate, password_validation, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import PasswordResetForm as PasswordResetFormBase
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext_lazy as _

from accounts.services import send_email_for_verify


User = get_user_model()


class MySetPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label= _("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", 'placeholder': 'Старый пароль'}
        ),
    )

    new_password1 = forms.CharField(
        max_length=128,
        label='Новый пароль',
        help_text=password_validation.password_validators_help_text_html(),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите новый пароль'
        })
    )

    new_password2 = forms.CharField(
        max_length=128,
        label='Подтверждение нового пароля',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Повторите новый пароль'
        })
    )


class UserSingUp(UserCreationForm):

    email = forms.EmailField(
        label="email",
        max_length=254,
        widget=forms.EmailInput(attrs={"class": "email"}),
    )

    class Meta:
        model = User
        fields = ('username', 'email')


class LoginForm(AuthenticationForm):
    confirm_email = False

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:

            self.user_cache = authenticate(
                self.request, email=username, password=password
            )

            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

            if not self.user_cache.email_verified:

                send_email_for_verify(self.request, self.user_cache)

                self.confirm_email = True

                raise ValidationError(
                    'Адрес электронной почты не подтвержден. Пожалуйста, проверьте свой адрес электронной почты.',
                    code="invalid_login",
                    params={'username': self.username_field.verbose_name},
                )
        return self.cleaned_data


class PasswordResetForm(PasswordResetFormBase):
    def clean(self):
        print('-------123---->')
        email = self.cleaned_data.get("email")
        if not User.objects.filter(email__iexact=email, email_verified=True).exists():
            raise ValidationError("Нет аккаунта с такой почтой или она не подтверждена!")

        return self.cleaned_data

class MyAuthenticationForm(AuthenticationForm):

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        print(username, password)
        if username is not None and password:

            self.user_cache = authenticate(
                self.request, email=username, password=password
            )

            print('-->', self.user_cache)

            if self.user_cache is None:
                print(self.get_invalid_login_error())
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

            if not self.user_cache.email_verified:

                send_email_for_verify(self.request, self.user_cache)

                raise ValidationError(
                    'Email not verified. Please check your email and try again.',
                    code="invalid_login",
                    params={'username': self.username_field.verbose_name},
                )

        return self.cleaned_data
