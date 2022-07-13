from django.shortcuts import render
# Create your views here.
from newgame.models import TourN
from newgame.utility import score_field


def index(request):
    name = None
    tour = TourN.objects.last()
    last_game = tour.games_list[-1][score_field]
    for names in last_game:
        if names['score'] == 5:
            name = names['user_name']
    print(name)
    champ = {'champion': name}

    return render(request, 'index.html', context=champ)


def records_page(request):
    context = {'content_text': "welcome to records page", }
    return render(request, 'records.html', context)


