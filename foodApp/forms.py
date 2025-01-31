from  django import  forms

class MenusFrom(forms.Form):
    DISPO = (
        ("O/Y", "OUI/YES"),
        ("N/N", "NON/NO"),
    )
    nomMenu = forms.CharField(label="Nom du produit :", max_length=128, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Entrez le nom du produit',
    }))
    composition = forms.CharField(label="Composition du produit :", max_length=128, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Entrez le nom du produit',
    }))
    categorie = forms.CharField(label="Nom du produit :", max_length=128, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Entrez le nom du produit',
    }))

    prixUnitaire = forms.FloatField(label="Prix Unitaire du produit :", initial=0, required=True,
                                    widget=forms.TextInput(attrs={
                                        'placeholder': 'Entrez le prix du menu',
                                    }))
    disponible = forms.Select(choices=DISPO)



    #image = forms.ImageField(label="Vous pouvez ajouter une image du produit :", required=True,
                             #widget=forms.ClearableFileInput(attrs={
                                # 'accept': 'image/*',

                            # }))

class ClientsForm(forms.Form):
    pass
