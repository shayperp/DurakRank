from django.forms import forms

from newgame.models import Users, Game, TourN


class InputNewNameForm(forms.Form):
    class Meta:
        model = Users
        fields = ["user_id", 'user_name']


class InputNewGameForm(forms.Form):
    class Meta:
        model = Game
        fields = ['game_name', 'game_users']


class EndGameForm(forms.Form):
    class Meta:
        model = TourN
        fields = ['tournament_id', 'games_list']



