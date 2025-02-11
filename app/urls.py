from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainPage.as_view(), name='Reels Scaner'),
    path('about/', views.About.as_view(), name='About'),
    path('privacy_policy/', views.privacy_policy, name='Privacy policy'),
    path('offer/', views.the_offer, name='The offer'),
    path('successful/', views.successful, name='Successful'),
    path('compilations/', views.compilations, name='Compilations'),
    path('compilations/<int:category>', views.compilations),
    path('bookmarks/', views.bookmarks, name='Bookmarks'),
    path('bookmarks/<int:folder_id>', views.bookmarks, name='BookmarksFolders'),
    path('add_authors/', views.add_authors),
    path('add_authors/add/', views.add_authors_post),
]
