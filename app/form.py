from django import forms
from app.models import Reels, Categories, MainChapters, Authors, BookmarksFolders
from accounts.models import User


class AddAuthorsForm(forms.Form):

    authors = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    main_categories = forms.ModelChoiceField(queryset=MainChapters.objects.all(), label="Main Category")

    categories = forms.ModelMultipleChoiceField(queryset=Categories.objects.all(), label="Categories")


class AddBookmarkFolder(forms.Form):

    name = forms.CharField(widget=forms.TextInput(attrs={'name': 'name'}))


