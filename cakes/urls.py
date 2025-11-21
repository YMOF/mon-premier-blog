from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),  # page principale / liste des recettes
    path('recette/creer/', views.creation_recette, name='creation_recette'),
    path('recette/<int:recette_id>/modifier/', views.modifier_recette, name='modifier_recette'),
    path('recette/<int:recette_id>/supprimer/', views.supprimer_recette, name='supprimer_recette'),  # <- IMPORTANT

]
