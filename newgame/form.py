from django.forms import forms

from newgame.models import Users


class InputNewNameForm(forms.Form):
    class Meta:
        model = Users
        fields = ["user_id", 'user_name']
# class NewGameForm(forms.Form):
#     players = forms.
