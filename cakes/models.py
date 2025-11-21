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

@receiver(post_migrate)
def create_default_recipes(sender, **kwargs):
    if sender.name == 'cakes':
        if not Recette.objects.exists():
            Recette.objects.create(
                nom="Gâteau au chocolat",
                ingredients="200g chocolat, 150g beurre, 150g sucre, 4 œufs, 70g farine",
                instructions="Faire fondre le chocolat et le beurre, mélanger avec le sucre et les œufs, ajouter la farine, cuire 25min à 180°C."
            )
            Recette.objects.create(
                nom="Brownie aux noix",
                ingredients="150g chocolat, 100g beurre, 100g sucre, 2 œufs, 50g farine, 50g noix",
                instructions="Faire fondre le chocolat et le beurre, mélanger avec sucre et œufs, ajouter farine et noix, cuire 20min à 180°C."
            )
            Recette.objects.create(
                nom="Space cake",
                ingredients="150g chocolat, 100g beurre, 100g sucre, 2 œufs, 50g farine, 50g noix",
                instructions="Faire fondre le chocolat et le beurre, mélanger avec sucre et œufs, ajouter farine et noix, cuire 20min à 180°C."
            )
            Recette.objects.create(
                nom="Gâteau au citron",
                ingredients="200g farine, 150g sucre, 100g beurre, 3 œufs, jus et zestes de 2 citrons, 1 sachet levure chimique",
                instructions="Mélanger sucre et beurre, ajouter œufs, farine et levure, puis le jus et zestes de citron. Cuire 30 min à 180°C."
            )