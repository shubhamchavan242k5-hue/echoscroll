from django.urls import path
from .views import get_music_feed, home

urlpatterns = [
    path('', home, name='home'), # खाली रास्ता मतलब होम पेज
    path('api/feed/', get_music_feed, name='music_feed'),
]