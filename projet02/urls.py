from django.urls import path
from .views import game_view, index

urlpatterns = [
    path('', index, name='projet02-index'),
    path('game/', game_view, name='game_view'),
]
