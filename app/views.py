from django.shortcuts import render, HttpResponse
from app.logic import add_new_authors
from app.form import AddAuthorsForm

from app.service import MainPage

def main_page(request):
    return MainPage(request).render()


def add_authors(request):

    #add_new_authors(['askar'], 4)

    return render(request, 'add_authors.html', {'form': AddAuthorsForm})


def add_authors_post(request):
    # получаем из данных запроса POST отправленные через форму данные
    authors = request.POST.get("authors", "Undefined")
    tag = request.POST.get("categories", "Undefined")

    stat = add_new_authors(authors, int(tag))

    return HttpResponse(f"<h2>Добавлено {stat['added_authors']} авторов</h2><h2>Изменено {stat['edit_authors']} авторов</h2>")

