
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    #/foodApp/ URL menant vers à la page d'acceuil
    path('', views.base, name='base'),
    path('acceuil', views.acceuil, name='acceuil'),

    path('ajoutMenu/', views.ajoutMenu, name='ajoutMenu'),
    #path('ajoutProduit/', views.ajoutProduit, name='ajoutProduit'),
    path('listeMenu/', views.listeMenu, name='listeMenu'),
    #path('listeCategorie/', views.listeCategorie, name='listeCategorie'),

]
