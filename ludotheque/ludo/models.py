from django.db import models

class Categorie(models.Model):
    nom_cat = models.CharField(max_length=100)
    descriptif_cat = models.TextField(null=True, blank=True)

    def __str__(self):
        chaine = f"{self.nom_cat}"
        return chaine

    def dico_cat(self):
        return {"nom_cat": self.nom_cat, "descriptif_cat": self.descriptif_cat}

class Jeux(models.Model):
    titre_jeux = models.CharField(max_length=100)
    annee_jeux = models.IntegerField(blank=False)
    image_jeux = models.ImageField(upload_to='photo',verbose_name='My Photo')
    editeur_jeux = models.CharField(max_length=100)
    auteur_jeux = models.CharField(max_length=100)
    categorie_jeux = models.ForeignKey("Categorie", on_delete=models.CASCADE)

    def __str__(self):
        chaine2 = f"{self.titre_jeux}"
        return chaine2

    def dico_jeux(self):
        return {"titre_jeux": self.titre_jeux, "anne_jeux": self.annee_jeux, "image_jeux": self.image_jeux, "editeur_jeux": self.image_jeux, "auteur_jeux": self.auteur_jeux, "categorie_jeux": self.categorie_jeux}


class Auteurs(models.Model):
    nom_aut = models.CharField(max_length=100)
    prenom_aut = models.CharField(max_length=100)
    age_aut = models.IntegerField(blank=False)
    photo_aut = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        chaine3 = f"{self.nom_aut} {self.prenom_aut}"
        return chaine3

    def dico_aut(self):
        return {"nom_aut": self.nom_aut, "prenom_aut": self.prenom_aut, "age_aut": self.age_aut, "photo_aut": self.photo_aut}

class Joueurs(models.Model):
    nom_j = models.CharField(max_length=100)
    prenom_j = models.CharField(max_length=100)
    mail_j = models.EmailField(blank=True, null=True)
    mdp_j = models.CharField(max_length=100, blank=True, null=True)
    choix = models.TextChoices('PROFESSIONNEL', 'PARTICULIER')
    type_j = models.CharField(blank=True, choices=choix.choices, max_length=10)

    def __str__(self):
        chaine4 = f"{self.nom_j}"
        return chaine4

    def dico_j(self):
        return {"nom_j": self.nom_j, "prenom_j": self.prenom_j, "mail_j": self.mail_j, "mdp_j": self.mdp_j, "type_j": self.type_j}

class Commentaires(models.Model):
    jeux = models.ForeignKey("jeux", on_delete=models.CASCADE)
    joueurs = models.ForeignKey("joueurs", on_delete=models.CASCADE)
    note = models.IntegerField(blank=False)
    commentaire = models.TextField(null=True, blank=True)
    date = models.DateField(blank=True, null=True)