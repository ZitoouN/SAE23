from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms

class Categorie(ModelForm):
    class Meta :
        model = models.Categorie
        fields = ('nom', 'descriptif')
        labels = {
            'nom' : _('Nom'),
            'descriptif' : _('Descriptif',)
        }

class Jeux(ModelForm):
    class Meta :
        model = models.Jeux
        fields = ('titre', 'annee', 'image', 'editeur', 'auteur', 'categorie')
        labels = {
            'titre' : _('Nom'),
            'annee' : _('Descriptif'),
            'image' : _('Image'),
            'editeur' : _('Editeur'),
            'auteur' : _('Auteur'),
            'categorie' : _('Categorie'),
        }

class Auteurs(ModelForm):
    class Meta :
        model = models.Auteurs
        fields = ('nom', 'prenom', 'age', 'photo')
        labels = {
            'nom' : _('Nom'),
            'prenom' : _('Prenom'),
            'age' : _('Age'),
            'photo' : _('Photo'),
        }

class Joueurs(ModelForm):
    class Meta :
        model = models.Joueurs
        fiels = ('nom', 'prenom', 'prenom', 'mail', 'mdp', 'type')
        labels = {
            'nom': _('Nom'),
            'prenom': _('Prenom'),
            'mail' : _('Mail'),
            'mdp' : _('Mot de passe'),
            'type' : _('Type'),
        }

class Commentaires(ModelForm):
    class Meta :
        model = models.Commentaires
        fields = ('jeux', 'joueurs', 'note', 'commentaire', 'date')
        labels = {
            'jeux' : _('Jeux'),
            'joueurs' : _('Joueurs'),
            'note' : _('Note'),
            'commentaire' : _('Commentaire' ),
            'date' : _('Date'),
        }