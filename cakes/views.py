from django.shortcuts import render, get_object_or_404, redirect
from .models import Recette
from django.shortcuts import get_object_or_404, redirect, render
from .models import Recette
from .utils import appeler_ollama
from django.db.models import Q
import logging
from django.http import JsonResponse
logger = logging.getLogger(__name__)


def accueil(request):
    query = request.GET.get('q')       # pour la barre de recherche (optionnel)
    generer = request.GET.get('gen')   # pour Ollama
    resultat_ollama = None

    #  Gestion recherche (optionnel)
    if query:
        mots = query.split()
        q_object = Q()
        for mot in mots:
            q_object |= Q(nom__icontains=mot) | Q(ingredients__icontains=mot)
        cakes_recette = Recette.objects.filter(q_object).distinct()
    else:
        cakes_recette = Recette.objects.all()

    #  Appel Ollama si demandé
    if generer:
        if query:  # si l'utilisateur a écrit quelque chose dans la barre
            prompt = f"Propose une recette simple de {query}"
        else:  # si la barre est vide, prompt par défaut
            prompt = "Propose une recette simple de gâteau au chocolat"
        resultat_ollama = appeler_ollama(prompt)
    #  Rendu
    return render(request, 'index.html', {
        'cakes_recette': cakes_recette,
        'resultat_ollama': resultat_ollama,
        'query': query
    })

# Création d'une recette        formulaire uniquement= raise forms.ValidationError("Veuillez remplir tous les champs")
def creation_recette(request):
    if request.method == 'POST': # POST -> Renvoie ce quel 'utilisatuer envoie. Si le formulaire est vide -> GET
        nom = request.POST.get('nom')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')
# une fois ajt va dans la bdd Models.py
        if not nom or not ingredients or not instructions:
            erreur = "Veuillez remplir tous les champs."
            return render(request, 'creation_recette.html', {
                'error': erreur,
                'nom': nom,
                'ingredients': ingredients,
                'instructions': instructions
            })
        Recette.objects.create(nom=nom, ingredients=ingredients, instructions=instructions)
        return redirect('accueil')  # Redirige vers la page index après ajout

    return render(request, 'creation_recette.html')

# python
def modifier_recette(request, recette_id):
    recette = get_object_or_404(Recette, id=recette_id)

    if request.method == "POST":
        nom = (request.POST.get('nom') or '').strip()
        ingredients = (request.POST.get('ingredients') or '').strip()
        instructions = (request.POST.get('instructions') or '').strip()

        if not nom or not ingredients or not instructions:
            erreur = "Veuillez remplir tous les champs."
            return render(request, 'modifier_recette.html', {
                'recette': recette,
                'error': erreur,
                'nom': nom,
                'ingredients': ingredients,
                'instructions': instructions
            })

        try:
            recette.nom = nom
            recette.ingredients = ingredients
            recette.instructions = instructions
            recette.save()
            return redirect('accueil')
        except Exception:
            logger.exception("Erreur lors de la sauvegarde de la recette id=%s", recette_id)
            erreur = "Une erreur serveur est survenue lors de l'enregistrement. Réessaye plus tard."
            return render(request, 'modifier_recette.html', {
                'recette': recette,
                'error': erreur,
                'nom': nom,
                'ingredients': ingredients,
                'instructions': instructions
            })

    return render(request, 'modifier_recette.html', {
        'recette': recette,
        'nom': recette.nom,
        'ingredients': recette.ingredients,
        'instructions': recette.instructions
    })

# python
def supprimer_recette(request, recette_id):
    recette = get_object_or_404(Recette, id=recette_id)
    if request.method == 'POST':
        recette.delete()
        return redirect('accueil')
    return render(request, 'confirmer_suppression.html', {'recette': recette})

#json
def api_ingredients(request, recette_id):
    # Sécurité : On récupère l'objet ou erreur 404
    try:
        recette = Recette.objects.get(id=recette_id)
        # On transforme la chaîne d'ingrédients en liste (pour le côté "non trivial")
        # Si tes ingrédients sont séparés par des virgules dans ta BDD :
        liste_ing = recette.ingredients.split(',')
        return JsonResponse({'ingredients': liste_ing})
    except Recette.DoesNotExist:
        return JsonResponse({'error': 'Introuvable'}, status=404)