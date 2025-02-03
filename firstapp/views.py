from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages

from .forms import CategorieForm, ProduitForm

from .models import Categorie, Produit

# git config --global core.autocrlf true

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

def supprimerProduit(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        if id:


            produit = get_object_or_404(Produit, id=id)
            produit.delete()
            messages.success(request, f"{produit.nom} a été supprimer avec succès")
            return redirect('listeProduit')
        else:
            messages.error(request, "Une erreur s'est produite lors de la suppression")
    else:
        return HttpResponse("Vous essayez d'utiliser une méthode non autorisée")
