from django.db import models



# Create your models here.
class Categorie(models.Model):

    titre = models.CharField(max_length=128)
    description = models.TextField()
    dateAjout = models.DateTimeField(auto_now_add=True, null=True)
    # date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['-dateAjout']
    
    def __str__(self):
        return self.titre


class Produit(models.Model):
    nom = models.CharField(max_length=128, verbose_name="Nom du produit")
    prixUnitaire = models.FloatField(default=0,verbose_name="Prix unitaitaire du produit")


    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE,related_name='produits', verbose_name="Catégorie du produit")
    image = models.ImageField(upload_to='produits', blank=True, null=True, verbose_name="Image du produit")
    stock = models.IntegerField(default=0, verbose_name="Quantité du produit")
    dateAjout = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Date d'ajout")

    class Meta:
        ordering=['-dateAjout']
    

    def __str__(self):
        return self.nom

    
class Etudiant(models.Model):
    nom = models.CharField(max_length=128)
    prenom = models.CharField(max_length=128)
    filiere = models.CharField(max_length=64)
    
class UE(models.Model):
    codeUE = models.CharField(primary_key=True, max_length=64)
    nbreCredit = models.IntegerField()
    inscrits = models.ManyToManyField(Etudiant, through="Inscription")

class Inscription(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    ue = models.ForeignKey(UE, on_delete=models.CASCADE)
    annee = models.IntegerField()
    


    
    
    # class Meta:
    #     verbose_name = 'Produit'
    #     verbose_name_plural = 'Produits'
    #     def __str__(self):
    #         return self.nom
        

   



    