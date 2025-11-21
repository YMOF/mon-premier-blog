
from django.shortcuts import render, get_object_or_404, redirect
from .models import Recette

def accueil(request):
    cakes_recette = Recette.objects.all()
    return render(request, 'index.html', {'cakes_recette': cakes_recette})

# Création d'une recette
def creation_recette(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')

        Recette.objects.create(nom=nom, ingredients=ingredients, instructions=instructions)
        return redirect('accueil')  # Redirige vers la page index après ajout

    return render(request, 'creation_recette.html')


def modifier_recette(request, recette_id):
    recette = get_object_or_404(Recette, id=recette_id)

    if request.method == "POST":
        recette.nom = request.POST.get('nom')
        recette.ingredients = request.POST.get('ingredients')
        recette.instructions = request.POST.get('instructions')
        recette.save()
        return redirect('accueil')  # Redirige vers l'index après modification

    return render(request, 'modifier_recette.html', {'recette': recette})


def supprimer_recette(request, recette_id):
    recette = get_object_or_404(Recette, id=recette_id)
    recette.delete()
    return redirect('accueil')  # Redirige vers l'index après suppression

