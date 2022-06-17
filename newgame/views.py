from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from newgame.models import Game, Tournament, Users
from newgame.serialzers import GameSerializer, TournamentSerializer, UsersSerializer
loser = 5


def new_app_page(request):
    users_name = []
    user = Users.objects.all()
    user_serializer = UsersSerializer(user, many=True)
    users_list = user_serializer.data
    for users in users_list:
        for key, value in users.items():
            if key == 'user_name':
                users_name.append(value)
    return render(request, 'new_game.html', {'users': users_name})


def save_end_game(request, results):
    if request.method == "Post":
        return print("ok")
    #   db.insert_one(models.Game(results))


def save_champion(request, results):
    for player, score in results.items():
        if score == loser:
            print(player)
    #  db.update_one("champion", player)
    context = {"champion": player}
    return render(request, context)


def game_api(request, id=0):
    if request.method == 'GET':
        game = Game.objects.all()
        game_serializer = GameSerializer(game, many=True)
        return JsonResponse(game_serializer.data, safe=False)
    elif request.method == 'POST':
        game_data = JSONParser().parse(request)
        game_serializer = GameSerializer(data=game_data)
        if game_serializer.is_valid():
            game_serializer.save()
            return JsonResponse("Add successful")
        return JsonResponse("faild", safe=False)
    elif request.method == "PUT":
        game_data = JSONParser.parse(request)
        game = Game.objects.get(game_id=game_data['game_id'])
        game_serializer = GameSerializer(game, data=game_data)
        if game_serializer.is_valid():
            game_serializer.save()
            return JsonResponse("update successfully ", safe=False)
        return JsonResponse("Faild ")
    elif request.method == 'DELETE':
        game = Game.objects.get(game_id=id)
        game.delete()
        return JsonResponse("deleted", safe=False)
