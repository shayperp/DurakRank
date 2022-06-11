from django.shortcuts import render


def new_app_page(request):
    return render(request, 'new_game.html')
