from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

#from .forms import CategorieForm, ProduitForm

from .models import Menus, Clients
from  .forms import MenusForm, ClientsForm


# git config --global core.autocrlf true

# Create your views here
#la vue pour afficher l'acceuil
def acceuil(request):
    return render(request, 'acceuil.html')
def base(request):
    return render(request, 'base.html')



def ajoutMenu(request):
    if request.method == 'POST':
        formsMenu = MenusForm(request.POST)
        if formsMenu.is_valid():
            nomMenu = formsMenu.cleaned_data['nomMenu']
            composition = formsMenu.cleaned_data['composition']
            categorie = formsMenu.cleaned_data['categorie']
            prixUnitaire = formsMenu.cleaned_data['prixUnitaire']
            disponible = formsMenu.cleaned_data['disponible']

            menu = Menus(nomMenu=nomMenu, composition=composition, categorie=categorie, prixUnitaire=prixUnitaire, disponible=disponible)
            menu.save()
            return redirect('listeMenu')  # Redirection vers la page de liste des catégories
        else:
            print(formsMenu.errors)

    else:
        formsMenu = MenusForm()

    return render(request, 'ajoutMenu.html', {'formsMenu': formsMenu})


"""
        forms = CustomUserCreationForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('connexion')
    else:
        forms = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': forms})

"""


def ajoutClient(request):
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
            return redirect('listeProduit')  # Redirection vers la page de liste des produits

    else:
        forms = ProduitForm()
    return render(request, 'ajoutProduit.html', {'forms': forms})


def listeProduit(request):
    produits = Produit.objects.all()

    context = {"produits": produits}
    if not produits.exists:
        message = "Aucun produit n'est enregistré"

        return render(request, "listeProduit.html", {"message": message})

    return render(request, "listeProduit.html", context)


def listeMenu(request):
    menus = Menus.objects.all()

    context = {"menus": menus}
    if not menus.exists:
        message = "Aucun produit n'est enregistré"

        return render(request, 'listeMenu.html', {"message": message})

    return render(request, 'listeMenu.html', context)


def supprimerProduit(request):
    if request.method == 'GET':
        produit = Produit.objects.get(id)
        produit.delete()