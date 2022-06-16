from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class CategorieForm(ModelForm):
    class Meta :
        model = models.Categorie
        fields = ('nom_cat', 'descriptif_cat')
        labels = {
            'nom_cat' : _('Nom de la catégorie'),
            'descriptif_cat' : _('Descriptif'),
        }

class JeuxForm(ModelForm):
    class Meta :
        model = models.Jeux
        fields = ('titre_jeux', 'annee_jeux', 'image_jeux', 'auteur_jeux', 'categorie_jeux')
        labels = {
            'titre_jeux' : _('Titre du jeu'),
            'annee_jeux' : _('Annee du jeu'),
            'image_jeux' : _('Image du jeu'),
            'auteur_jeux' : _('Auteur du jeu'),
            'categorie_jeux' : _('Categorie du jeu'),
        }

class AuteursForm(ModelForm):
    class Meta :
        model = models.Auteurs
        fields = ('nom_aut', 'age_aut', 'photo_aut')
        labels = {
            'nom_aut' : _('Nom du studio '),
            'age_aut' : _('Date de création '),
            'photo_aut' : _('Icone du studio '),
        }

class JoueursForm(ModelForm):
    class Meta :
        model = models.Joueurs
        fields = ('nom_j', 'prenom_j', 'prenom_j', 'mail_j', 'mdp_j', 'type_j')
        labels = {
            'nom_j': _('Nom du Joueur'),
            'prenom_j': _('Prenom du Joueur'),
            'mail_j' : _('Mail du Joueur'),
            'mdp_j' : _('Mot de passe du Joueur'),
            'type_j' : _('Type de Joueur'),
        }

class CommentairesForm(ModelForm):
    class Meta :
        model = models.Commentaires
        fields = ('jeux_com', 'joueurs_com', 'note_com', 'commentaire_jeu', 'date_com')
        labels = {
            'jeux_com' : _('Jeux commenté'),
            'joueurs_com' : _('Joueur'),
            'note_com' : _('Note du commentaire'),
            'commentaire_jeu' : _('Commentaire Jeu' ),
            'date_com' : _('Date du Commentaire'),
        }