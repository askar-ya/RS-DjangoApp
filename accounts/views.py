from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.http import HttpResponseForbidden

from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_decode
from django.views.generic import TemplateView
from app.models import BookmarksFolders

from .forms import UserSingUp, MyAuthenticationForm, MySetPasswordForm
from django.views import View

from .services import send_email_for_verify
from django.contrib.auth.tokens import default_token_generator as token_generator



User = get_user_model()

class MyLoginView(LoginView):
    form_class = MyAuthenticationForm


class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'registration/Profile.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)

        else:
            return HttpResponseForbidden()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['user_password_form'] = MySetPasswordForm(self.request.user)
        return context

    def post(self, request, *args, **kwargs):

        if 'user_password_form' in request.POST:
            form = MySetPasswordForm(request.user, request.POST)
            if form.is_valid():
                form.save()

                print('Пароль успешно изменён.')
                return self.get(request, *args, **kwargs)
            else:
                context = self.get_context_data(**kwargs)
                context['user_password_form'] = form
                return render(request, self.template_name, context)
        else:
            return self.get(request, *args, **kwargs)


class Registration(View):

    template_name = 'registration/signup.html'

    def get(self, request):
        context = {
            'form': UserSingUp(),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserSingUp(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(email=email, password=raw_password)

            BookmarksFolders(user=user, name='dump').save()

            send_email_for_verify(request, user)

            return redirect('confirm_email')

        context = {'form': form}

        return render(request, self.template_name, context)


class VerifyEmail(View):

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)
        if user is not None and token_generator.check_token(user, token):
            user.email_verified = True
            user.save()
            login(request, user)
            return redirect('/')
        return redirect('invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User._default_manager.get(pk=uid)
        except (
                TypeError,
                ValueError,
                OverflowError,
                User.DoesNotExist,
                ValidationError,
        ):

            user = None

        return user