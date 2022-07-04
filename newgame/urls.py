from django.urls import path
from newgame import views

urlpatterns = [
    path('', views.new_app_page, name='new_game'),
    path('quick-game', views.quick_tournament, name='quick_game'),
    path('game_page', views.start_tournament, name='game_page'),
    path('end_of_game', views.end_of_game, name='end_of_game'),
]

