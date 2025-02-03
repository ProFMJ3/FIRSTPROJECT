
from django.urls import path
from . import views

urlpatterns = [
    path('', views.acceuil, name='acceuil'),
    path('ajoutCategorie/', views.ajoutCategorie, name='ajoutCategorie'),
    path('ajoutProduit/', views.ajoutProduit, name='ajoutProduit'),
    path('listeProduit/', views.listeProduit, name='listeProduit'),
    path('listeCategorie/', views.listeCategorie, name='listeCategorie'),
    
    path('supprimer<int:id>/', views.supprimerProduit, name='supprimerProduit'),

]
