from django.shortcuts import render
from django.http import HttpResponse
from .models import Recette

def accueil(request):
    return HttpResponse("Bienvenue sur le blog !")

def post_list(request):
    return render(request, 'blog/post_list.html', {})

