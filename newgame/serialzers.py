from newgame.models import Game, Tournament, Users
from rest_framework import serializers


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('game_id', 'game_name', 'game_users')


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ('Tournament_id', 'date', 'games_score')


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('user_name', 'user_id')
