from app.models import Authors, Categories


def add_new_authors(authors: str, category_id: int):


    authors = authors.split('\r\n')

    added_authors = 0
    edit_authors = 0
    for author in authors:

        try:
            author_data = Authors.objects.get(nick=author)
            category_data = Categories.objects.filter(authors=author_data.id)

            if category_id not in category_data.values_list('id', flat=True):
                category = Categories.objects.get(id=category_id)
                category.authors_set.add(author_data.id)
            edit_authors += 1
        except Authors.DoesNotExist:
            author = Authors.objects.create(nick=author)

            category = Categories.objects.get(id=category_id)
            category.authors_set.add(author.id)
            added_authors += 1

    return {"added_authors": added_authors, "edit_authors": edit_authors}
