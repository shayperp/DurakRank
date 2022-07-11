import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.datetime_safe import date
from djongo import models
from django import forms


class Users(models.Model):
    user_name = models.CharField(max_length=20)


class Game(models.Model):
    game_name = models.CharField(max_length=30, default='Game number ')
    game_users = models.JSONField()


class GameScore(models.Model):
    user_name = models.CharField(max_length=20, primary_key=True, )
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    class Meta:
        managed = False

    def __getitem__(self, item):
        return getattr(self, item)


class SingleGameAbstract(models.Model):
    game_score = models.ArrayField(model_container=GameScore)
    game_name = models.CharField(max_length=30, default="Game number", primary_key=True, )

    class Meta:
        managed = False

    def __getitem__(self, item):
        return getattr(self, item)


class SingleGame(forms.ModelForm):
    class Meta:
        model = SingleGameAbstract
        fields = ('game_score', 'game_name')


class TourN(models.Model):
    id = models.BigAutoField(primary_key=True)
    play_date = models.DateField(default=date.today)
    games_list = models.ArrayField(model_container=SingleGameAbstract, model_form_class=SingleGame)
    objects = models.DjongoManager()
