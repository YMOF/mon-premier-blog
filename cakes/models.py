from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver

class Recette(models.Model):
    nom = models.CharField(max_length=100)
    ingredients = models.TextField(default="Ingrédients à définir")
    instructions = models.TextField(default="Instructioons à définir")
    # ajoute d’autres champs si besoin

    def __str__(self):
        return self.nom
# ma base de donnée
# models.CharField : c'est une donnée courte.
#
# models.TextField : ces textes peuvent être très longs.
#
# default="..." : par defaut il y aura l'écriture. crées une recette sans remplir tous les champs par erreur.
#
# __str__(self) :  tu vois le nom de la recette (ex: "Gâteau au chocolat") au lieu de "Recette object (1)".