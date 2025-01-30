# Generated by Django 5.1.2 on 2025-01-26 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_rename_pu_produit_prixunitaire_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='dateAjout',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='produit',
            name='dateAjout',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='produit',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='produits'),
        ),
        migrations.AddField(
            model_name='produit',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
