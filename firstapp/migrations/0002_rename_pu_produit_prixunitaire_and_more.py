# Generated by Django 5.1.3 on 2024-12-13 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produit',
            old_name='pu',
            new_name='prixUnitaire',
        ),
        migrations.RenameField(
            model_name='ue',
            old_name='inscrit',
            new_name='inscrits',
        ),
        migrations.AlterField(
            model_name='categorie',
            name='titre',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='filiere',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='ue',
            name='codeUE',
            field=models.CharField(max_length=64, primary_key=True, serialize=False),
        ),
    ]
