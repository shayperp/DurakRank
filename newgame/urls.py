from django.urls import path

from newgame import views

urlpatterns = [
    path('', views.new_app_page, name='new_game'),
]