from django.contrib import admin

from .models import Categorie, Produit



@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['titre', 'description']
    list_filter = ['titre', 'dateAjout']
    search_fields = ['titre','description']
    
@admin.register(Produit)
class ModelNameAdmin(admin.ModelAdmin):

    list_display = ['nom', 'image', 'prixUnitaire', 'stock', 'categorie', 'dateAjout']
    list_filter = ['categorie', 'dateAjout']
    search_fields = ['nom', 'prixUnitaire']
    
