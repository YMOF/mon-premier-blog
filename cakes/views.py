
from django.shortcuts import render, get_object_or_404, redirect
from .models import Recette

def accueil(request):
    cakes_recette = Recette.objects.all()
    return render(request, 'index.html', {'cakes_recette': cakes_recette})

# Création d'une recette        formulaire uniquement= raise forms.ValidationError("Veuillez remplir tous les champs")
def creation_recette(request):
    if request.method == 'POST': # POST -> Renvoie ce quel 'utilisatuer envoire. Si le formulaire est vide -> GET
        nom = request.POST.get('nom')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')
# une fois ajt va dans la bdd Models.py
        if not nom or not ingredients or not instructions:
            erreur ="Veuillez remplir tous les champs."
            return render(request, 'creation_recette.html', {'error': "Veuillez remplir tous les champs."})

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

        if not nom or not ingredients or not instructions:
            erreur ="Veuillez remplir tous les champs."
            return render(request, 'modifier_recette.html', {'error': "Veuillez remplir tous les champs."})
        return redirect('accueil')  # Redirige vers l'index après modification

    return render(request, 'modifier_recette.html', {'recette': recette})


def supprimer_recette(request, recette_id):
    recette = get_object_or_404(Recette, id=recette_id)
    recette.delete()
    return redirect('accueil')  # Redirige vers l'index après suppression

