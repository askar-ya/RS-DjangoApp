from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name='Reels Scaner'),
    path('about/', views.About.as_view(), name='About'),
    path('successful/', views.successful, name='Successful'),
    path('compilations/', views.compilations, name='Compilations'),
    path('compilations/<int:category>', views.compilations),
    path('bookmarks/', views.bookmarks, name='Bookmarks'),
    path('bookmarks/<int:folder_id>', views.bookmarks, name='BookmarksFolders'),
    path('add_authors/', views.add_authors),
    path('add_authors/add/', views.add_authors_post),
]
