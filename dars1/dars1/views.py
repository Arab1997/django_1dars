from django.shortcuts import render


def index(request):

    return render(request, 'dars1/index.html')
