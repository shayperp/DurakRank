from django.shortcuts import render
# Create your views here.


def index(request):

    return render(request, 'index.html')


def records_page(request):
    context = {'content_text': "welcome to records page", }
    return render(request, 'records.html', context)


