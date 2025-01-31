from email.policy import default
from random import choices

from django.db import models

# Create your models here.
class Menus(models.Model):
    DISPO = (
        ("O/Y", "OUI/YES"),
        ("N/N", "NON/NO"),
    )

    nomMenu = models.CharField(max_length=128)
    composition = models.CharField(max_length=128)
    descriptions = models.TextField()
    categorie = models.CharField(max_length=128)
    prixUnitaire = models.FloatField(min("0"), null=True)
    disponible = models.CharField(choices=DISPO, default="O/Y")
    dateAjout = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =['-dateAjout']


    def __str__(self):
        return self.nomMenu



class Clients(models.Model):
    nomClient = models.CharField(max_length=128)
    prenomsClient = models.CharField(max_length=128)
    adresse = models.CharField(max_length=128)
    telephone = models.CharField(max_length=128)
    dateAjout = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =['-dateAjout']

    def __str__(self):
        return self.nomClient



