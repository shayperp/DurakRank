from newgame.models import Users, TourN
from rest_framework import serializers


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['user_name']


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourN
        fields = ['id', 'play_date', 'games_list']
