from django.shortcuts import render, HttpResponse
from app.logic import add_new_authors
from app.form import AddAuthorsForm

from app.service import MainPage, Compilations, BookmarksView

from django.http import FileResponse
import os

def main_page(request):

    return MainPage(request).render()

def about(request):
    return render(request, template_name='About.html')

def successful(request):
    return render(request, template_name='Thanks.html')


def privacy_policy(request):
    return FileResponse(open('app/static/docs/privacy_policy.pdf', 'rb'), content_type='application/pdf')


def offer(request):
    return FileResponse(open('app/static/docs/offer.pdf', 'rb'), content_type='application/pdf')

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

