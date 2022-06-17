from datetime import datetime

from django.utils.datetime_safe import date
from djongo import models


class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    game_name = models.CharField(max_length=30, default='Game number ')
    game_users = models.JSONField(default={'Reem': '0', 'Shay': '0', 'Kobi': '0'})


class Tournament(models.Model):
    Tournament_id = models.AutoField(primary_key=True)
    play_date = models.DateField(default=date.today)
    games_score = models.JSONField(default={'Reem': '0', 'Shay': '0', 'Kobi': '0'})


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.user_name)





