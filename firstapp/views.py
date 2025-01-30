from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .forms import CategorieForm, ProduitForm

from .models import Categorie, Produit

# Create your views here
def acceuil(request):
    return render(request, 'acceuil.html')

def ajoutCategorie(request):
    if request.method == 'POST':
        forms = CategorieForm(request.POST)
        if forms.is_valid():
            titre = forms.cleaned_data['titre']
            description = forms.cleaned_data['description']
            categorie = Categorie(titre=titre, description=description)
            categorie.save()
            return redirect('listeCategorie')# Redirection vers la page de liste des catégories
        else:
            print(forms.errors)

    else:
        forms = CategorieForm()
    
    return render(request, 'ajoutCategorie.html', {'forms': forms})

"""
        forms = CustomUserCreationForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('connexion')
    else:
        forms = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': forms})

"""

def ajoutProduit(request):
    if request.method == 'POST':
        forms = ProduitForm(request.POST, request.FILES)
        if forms.is_valid():
            nom = forms.cleaned_data['nom']
            prixUnitaire = forms.cleaned_data['prixUnitaire']
            categorie = forms.cleaned_data['categorie']
            image = forms.cleaned_data['image']
            stock = forms.cleaned_data['stock']

            produit = Produit(nom=nom, prixUnitaire=prixUnitaire, categorie=categorie, image=image, stock=stock)
            produit.save()
            return redirect('listeProduit')# Redirection vers la page de liste des produits
        
    else:
        forms = ProduitForm()
    return render(request, 'ajoutProduit.html', {'forms': forms})
        
def listeProduit(request):
    produits = Produit.objects.all()

    context = {"produits":produits}
    if  not produits.exists:
        message = "Aucun produit n'est enregistré"
        
        return render(request, "listeProduit.html", {"message":message})
        

    return render(request, "listeProduit.html", context)

def listeCategorie(request):
    categories = Categorie.objects.all()

    context = {"categories":categories}
    if  not categories.exists:
        message = "Aucun produit n'est enregistré"
        
        return render(request, 'listeCategorie.html', {"message":message})
        

    return render(request, 'listeCategorie.html', context)