from django.forms import forms

from newgame.models import Users, Game


class InputNewNameForm(forms.Form):
    class Meta:
        model = Users
        fields = ["user_id", 'user_name']


class InputNewGameForm(forms.Form):
    class Meta:
        model = Game
        fields = ['id', 'game_users', 'game_name']

