from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.parsers import JSONParser
from newgame.models import Game, Tournament, Users
from newgame.serialzers import GameSerializer, TournamentSerializer, UsersSerializer
from newgame.form import InputNewNameForm, InputNewGameForm

loser = 5


def list_of_user():
    users_names = []
    user = Users.objects.all()
    user_serializer = UsersSerializer(user, many=True)
    users_list = user_serializer.data
    for users in users_list:
        for key, value in users.items():
            if key == 'user_name':
                users_names.append(value)
    return users_names


def new_app_page(request):
    if request.method == 'POST':
        new_user = InputNewNameForm(request.POST or None)
        users_list = list_of_user()
        if new_user is not None:
            name = new_user.data['user_name']
            if name not in users_list:
                user = Users(name)
                user.save()

    users_list = list_of_user()
    return render(request, 'new_game.html', {'users': users_list})


def game_form(request):
    if request.method == 'POST':
        input_form = InputNewGameForm(request.POST or None)
        print(input_form)
        player = input_form.data['game_users']
    return render(request, 'game_page.html', {'players': player})


def quick_game(request):
    context = {'players': ['Reem', 'Shay', 'Kobi']}
    tournament = Tournament()
    tournament.games_score = context
    return render(request, 'game_page.html', context)


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
