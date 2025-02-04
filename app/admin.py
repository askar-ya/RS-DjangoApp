from django.contrib import admin
from app.models import Reels, Authors, MainChapters, Categories, BookmarksFolders, Bookmarks


admin.site.register(MainChapters)
admin.site.register(Categories)
admin.site.register(Reels)
admin.site.register(Authors)
admin.site.register(BookmarksFolders)
admin.site.register(Bookmarks)
# Register your models here.
