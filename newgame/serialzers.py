from newgame.models import Users
from rest_framework import serializers


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('user_name', 'user_id')


#
# class TournamentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tournament
#         fields = ('Tournament_id', 'date', 'games_score')
