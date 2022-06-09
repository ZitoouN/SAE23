from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    descriptif = models.TextField(null=True, blank=True)

    def __str__(self):
        chaine = f"{self.nom}"
        return chaine

class Jeux(models.Model):
    titre = models.CharField(max_length=100)
    annee = models.IntegerField(blank=False)
    image = models.ImageField(upload_to='photo',verbose_name='My Photo')
    editeur = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    categorie = models.ForeignKey("categorie", on_delete=models.CASCADE)

    def __str__(self):
        chaine2 = f"{self.titre}"
        return chaine2

class Auteurs(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.IntegerField(blank=False)
    photo = models.ImageField(upload_to='photo',verbose_name='My Photo')

    def __str__(self):
        chaine3 = f"{self.nom}"
        return chaine3

class Joueurs(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    mail = models.EmailField(blank=True, null=True)
    mdp = models.CharField(max_length=100, blank=True, null=True)
    choix = models.TextChoices('PROFESSIONNEL', 'PARTICULIER')
    type = models.CharField(blank=True, choices=choix.choices, max_length=10)

    def __str__(self):
        chaine4 = f"{self.nom}"
        return chaine4

class Commentaires(models.Model):
    jeux = models.ForeignKey("jeux", on_delete=models.CASCADE)
    joueurs = models.ForeignKey("joueurs", on_delete=models.CASCADE)
    note = models.IntegerField(blank=False)
    commentaire = models.TextField(null=True, blank=True)
    date = models.DateField(blank=True, null=True)