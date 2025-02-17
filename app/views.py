from django.shortcuts import render, HttpResponse, redirect
from app.logic import add_new_authors
from app.form import AddAuthorsForm
from accounts.forms import UserSingUp, LoginForm
from django.views import View
from django.contrib.auth import login, authenticate
from app.service import Compilations, BookmarksView
from accounts.services import send_email_for_verify
from accounts.forms import PasswordResetForm

class PageWithForms(View):
    template_name = ''
    complete_reg = ''

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            print(user.has_quota())
        context = {
            'SingUpForm': UserSingUp(),
            'LoginForm': LoginForm(),
            'PasswordResetForm': PasswordResetForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        print(request.POST)
        context = {}
        if 'LoginForm' in request.POST:
            form = LoginForm(request, data=request.POST)
            if form.is_valid():
                email = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(email=email, password=password)  # Проверяем учетные данные
                if user is not None:
                    login(request, user)  # Выполняем вход
                    return redirect('Reels Scaner')  # Перенаправляем на главную страницу
            context = {'LoginForm': form, 'FormsErrors': 'LoginForm', 'SingUpForm': UserSingUp(), 'PasswordResetForm': PasswordResetForm()}
            if form.confirm_email:
                context['FormsErrors'] = 'EmailConfirmed'
                context['UserEmail'] = form.cleaned_data['username']

        elif 'SingUpForm' in request.POST:
            form = UserSingUp(request.POST)
            if form.is_valid():
                form.save()
                email = form.cleaned_data.get('email')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(email=email, password=raw_password)
                send_email_for_verify(request, user)
                context = {
                    'SingUpForm': UserSingUp(),
                    'LoginForm': LoginForm(),
                    'PasswordResetForm': PasswordResetForm(),
                    'FormsErrors': 'EmailConfirmed',
                    'UserEmail': email
                }
                if self.complete_reg == 'Successful':
                    return redirect(self.complete_reg)
                return redirect(self.complete_reg, context)
            context = {'SingUpForm': form, 'FormsErrors': 'SingUpForm', 'LoginForm': LoginForm(), 'PasswordResetForm': PasswordResetForm()}

        elif 'PasswordResetForm' in request.POST:
            form = PasswordResetForm(request.POST)
            if form.is_valid():
                form.save(request=self.request)
                context = {
                    'SingUpForm': UserSingUp(),
                    'LoginForm': LoginForm(),
                    'PasswordResetForm': form,
                    'FormsErrors': 'EmailConfirmed',
                    'UserEmail': form.cleaned_data.get('email')
                }
                return render(request, self.template_name, context)
            context = {'SingUpForm': UserSingUp(), 'FormsErrors': 'PasswordResetForm', 'LoginForm': LoginForm(),
                       'PasswordResetForm': form}

        return render(request, self.template_name, context)

class MainPage(PageWithForms):

    template_name = 'MainPage.html'
    complete_reg = 'Reels Scaner'

class About(PageWithForms):
    template_name = 'About.html'
    complete_reg = 'Successful'

def test(request):
    return render(request, 'test.html')


def privacy_policy(request):
    return render(request, 'PrivacyPolicy.html')

def the_offer(request):
    return render(request, 'TheOffer.html')

def successful(request):
    return render(request, template_name='Thanks.html')


def add_authors(request):
    return render(request, 'add_authors.html', {'form': AddAuthorsForm})


def add_authors_post(request):
    # получаем из данных запроса POST отправленные через форму данные
    authors = request.POST.get("authors", "Undefined")
    tag = request.POST.get("categories", "Undefined")

    stat = add_new_authors(authors, int(tag))

    return HttpResponse(f"<h2>Добавлено {stat['added_authors']} авторов</h2><h2>Изменено {stat['edit_authors']} авторов</h2>")


def compilations(request, category=False):

    print(category)

    return Compilations(request).render()

def bookmarks(request, folder_id=None):
    return BookmarksView(request).render(folder_id)

