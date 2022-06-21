from datetime import datetime

from django.utils.datetime_safe import date
from djongo import models
from django import forms


class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    game_users = models.JSONField(default={'Reem': '0', 'Shay': '0', 'Kobi': '0'})
    game_name = models.CharField(max_length=30, default='Game number')


class Tournament(models.Model):
    Tournament_id = models.AutoField(primary_key=True)
    play_date = models.DateField(default=date.today)
    games_score = models.JSONField(default={'Reem': '0', 'Shay': '0', 'Kobi': '0'})


class Users(models.Model):
    user_name = models.CharField(max_length=20)
    user_id = models.AutoField(primary_key=True)











