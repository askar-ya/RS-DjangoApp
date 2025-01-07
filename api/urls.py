from django.urls import path
from .views import ReelsList


urlpatterns = [
    path(r"reels/", ReelsList.as_view()),
]
