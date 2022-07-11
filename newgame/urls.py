from django.urls import path
from newgame import views

urlpatterns = [
    path('', views.new_app_page, name='new_game'),
    path('new_user', views.new_user, name='new_user_def'),
    path('quick-game', views.quick_tournament, name='quick_game'),
    path('game_page', views.start_tournament, name='game_page'),
    path('end_game', views.end_of_game, name='end_of_game'),
    path('game_continues', views.game_continues, name='game_continues'),
]
