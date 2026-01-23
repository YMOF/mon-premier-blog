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
