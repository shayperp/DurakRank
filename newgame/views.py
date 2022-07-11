from bson import ObjectId
from django.db.models.lookups import Range
from django.http import HttpRequest
from django.shortcuts import render, redirect
from newgame.models import Users, TourN
from newgame.serialzers import UsersSerializer, TournamentSerializer
from newgame.form import InputNewNameForm, InputNewGameForm, EndGameForm
from newgame.utility import *


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


def new_user(request):
    if request.method == 'POST':
        user_form_element = InputNewNameForm(request.POST or None)
        users_list = list_of_user()
        if user_form_element.is_valid():
            name = user_form_element.data['user_name']
            if name is not None:
                if name not in users_list:
                    user = Users(user_name=name)
                    user.save()
    return new_app_page(request)


def new_app_page(request):
    users_list = list_of_user()
    return render(request, 'new_game.html', {'users': users_list})


def game_form(request):
    if request.method == 'POST':
        if request.POST.is_valid():
            input_form = InputNewGameForm(request.POST or None)
            player = input_form.data['game_users']
        else:
            player = players_default
    return render(request, 'game_page.html', {'players': player})


def quick_game(request):
    pass


def start_tournament(request):
    game_stat = {}
    users = [None]
    if request.method == 'POST':
        input_form = InputNewGameForm(request.POST or None)
        if input_form.is_valid():
            if input_form.data['game_name'] is not None:
                users = request.POST.getlist(players_list)
                name = request.POST.get('game_name', False)
        score = [{'user_name': user, 'score': 0} for user in users]
        tournament = TourN()
        name = name if name is not None else quick_name
        tournament.games_list = [make_game(score, name)]
        tournament.save()
        game_stat[userName_field] = users
        game_stat[gameName_field] = name
        game_stat['tournament_id'] = tournament.pk
    else:
        pass

    return render(request, 'game_page.html', game_stat)


def quick_tournament(request):
    # tournament = TourN()
    # tournament.games_list = [make_game(quick_score, quick_name)]
    # tournament.save()
    game_stat = {userName_field: players_default, gameName_field: quick_name}
    return render(request, 'game_page.html', game_stat)


def end_of_game(request):
    if request.method == 'POST':
        input_form = EndGameForm(request.POST or None)
        if input_form.is_valid():
            if input_form.data is not None:
                values_players = request.POST.getlist('score[]')
                id_tour = request.POST.get('tournament_id', False)
                if id_tour is not None:
                    id_torun = id_tour.replace('/', '')
                    tour_serial = TourN.objects.filter(pk=id_torun)
                    tourn_obj = tour_serial[0]
                    first_game = tourn_obj.games_list[0][score_field]
                    i = int(0)
                    for users in first_game:
                        users['score'] = values_players[i]
                        i += 1
                    tourn_obj.games_list[0][score_field] = first_game
                    tourn_obj.save()

                else:
                    pass
                if values_players is not None:  # need to replace
                    pass

    return render(request, 'after_game_page.html')


def game_continues(request):
    pass

# def save_champion(request, results):
#     for player, score in results.items():
#         if score == loser:
#             print(player)
#     #  db.update_one("champion", player)
#     context = {"champion": player}
#     return render(request, context)


# def game_api(request, id=0):
#     if request.method == 'GET':
#         game = Game.objects.all()
#         game_serializer = GameSerializer(game, many=True)
#         return JsonResponse(game_serializer.data, safe=False)
#     elif request.method == 'POST':
#         game_data = JSONParser().parse(request)
#         game_serializer = GameSerializer(data=game_data)
#         if game_serializer.is_valid():
#             game_serializer.save()
#             return JsonResponse("Add successful")
#         return JsonResponse("faild", safe=False)
#     elif request.method == "PUT":
#         game_data = JSONParser.parse(request)
#         game = Game.objects.get(game_id=game_data['game_id'])
#         game_serializer = GameSerializer(game, data=game_data)
#         if game_serializer.is_valid():
#             game_serializer.save()
#             return JsonResponse("update successfully ", safe=False)
#         return JsonResponse("Faild ")
#     elif request.method == 'DELETE':
#         game = Game.objects.get(game_id=id)
#         game.delete()
#         return JsonResponse("deleted", safe=False)
