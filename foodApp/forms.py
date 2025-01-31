from  django import  forms

class MenusForm(forms.Form):
    DISPO = (
        ("", "Select"),
        ("O/Y", "OUI/YES"),
        ("N/N", "NON/NO"),
    )
    nomMenu = forms.CharField(label="Nom du menu :", max_length=128, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Entrez le nom du ménu',
    }))
    composition = forms.CharField(label="Composition du menu:", max_length=128, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'le ménu est composé de quoi ?',
    }))
    categorie = forms.CharField(label="Categorie :", max_length=128, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Le ménu appartient à quelle catégorie ?',
    }))

    prixUnitaire = forms.FloatField(label="Prix Unitaire du ménu :", initial=0, required=True,
                                    widget=forms.TextInput(attrs={
                                        'placeholder': 'Quel est le prix du ménu ?',
                                    }))
    disponible = forms.ChoiceField(label="Disponibilité", required=True, choices=DISPO, widget=forms.Select(attrs={'class': 'radio'}))



    #image = forms.ImageField(label="Vous pouvez ajouter une image du produit :", required=True,
                             #widget=forms.ClearableFileInput(attrs={
                                # 'accept': 'image/*',

                            # }))

class ClientsForm(forms.Form):
    pass
