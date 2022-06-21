from django.urls import path
from newgame import views

urlpatterns = [
    path('', views.new_app_page, name='new_game'),
    path('quick-game', views.quick_game, name='quick_game'),
    path('game_page', views.game_form, name='game_page'),
]

