from django.shortcuts import render


# Create your views here.

def index(request):
    context = {'index_text': "welcome to index page", }
    return render(request, 'index.html', context)


def records_page(request):
    context = {'content_text': "welcome to records page", }
    return render(request, 'records.html', context)


