from django.urls import path
from . import views


urlpatterns = [
    path('', views.accueil, name='accueil'),  # page d'accueil du blog
    path('posts/', views.post_list, name='post_list'),  # liste des posts
]
