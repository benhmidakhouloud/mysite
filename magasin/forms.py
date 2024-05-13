from django import forms  # Importez forms depuis Django
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Produit, Fournisseur, Commande

class ProduitForm(forms.ModelForm):  # Utilisez forms.ModelForm
    class Meta:
        model = Produit
        fields = "__all__"  # Utilisation de "__all__" pour inclure tous les champs du modèle

class FournisseurForm(forms.ModelForm):  # Utilisez forms.ModelForm
    class Meta:
        model = Fournisseur
        fields = "__all__"

class CommandeForm(forms.ModelForm):  # Utilisez forms.ModelForm
    class Meta:
        model = Commande
        fields = "__all__"  # ou les champs que vous souhaitez inclure
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')
class Meta(UserCreationForm.Meta):
    model = User
    fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')