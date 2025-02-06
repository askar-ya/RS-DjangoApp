from django.shortcuts import render, HttpResponse, redirect
from app.logic import add_new_authors
from app.form import AddAuthorsForm
from accounts.forms import UserSingUp
from django.views import View
from django.contrib.auth import login, authenticate, get_user_model
from django.template import RequestContext
import json
from app.service import MainPage, Compilations, BookmarksView

from accounts.services import send_email_for_verify

def main_page(request):

    return MainPage(request).render()


class About(View):
    template_name = 'About.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('Reels Scaner')
        context = {
            'SingUpForm': UserSingUp(),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserSingUp(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(email=email, password=raw_password)

            send_email_for_verify(request, user)

            return redirect('Successful')

        context = {'SingUpForm': form, 'errors': True}
        return render(request, self.template_name, context)


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

