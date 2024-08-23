from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_game, name='start_game'),
    path('play/', views.play_round, name='play_round'),
    path('game_over/', views.game_over, name='game_over'),
    path('summary/', views.game_summary, name='game_summary'),
]