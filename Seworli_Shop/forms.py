from django import forms
from .models import Drone, Appareil,Objectif,Accessoires


class DroneForm(forms.Form):
    ETAT = (
        ('neuf sous emballage','neuf sous emballage'),
        ('neuf jamais utilisé','neuf jamais utilisé'),
        ('bon état','bon état'),
        ('moyen','moyen'),)
    etat = forms.ChoiceField(choices=ETAT)
    class Meta:
        model = Drone
        fields = [
				'titre',
				'description',
				'image',
                'prix',]

class AccessoiresForm(forms.Form):
    ETAT = (
        ('neuf sous emballage','neuf sous emballage'),
        ('neuf jamais utilisé','neuf jamais utilisé'),
        ('bon état','bon état'),
        ('moyen','moyen'),)
    etat = forms.ChoiceField(choices=ETAT)
    class Meta:
        model = Accessoires
        fields = [
			    'titre',
				'description',
				'image',
                'prix',]




class AppareilForm(forms.Form):
	CHOICES = (
		('Reflexe','Reflexe'),
		('Hybride','Hybride'),
		('Bridge','Bridge'),
		('Compact','Compact'),)
	ETAT = (
        ('neuf sous emballage','neuf sous emballage'),
        ('neuf jamais utilisé','neuf jamais utilisé'),
        ('bon état','bon état'),
        ('moyen','moyen'),)
	sous_categorie = forms.ChoiceField(choices=CHOICES)
	etat = forms.ChoiceField(choices=ETAT)
	class Meta:
		model = Appareil
		fields = [
				'titre',
				'description',
				'image',
                'prix',]


class ObjectifForm(forms.Form):
	CHOICES = (
		('Panasonic-leica','Panasonic-leica'),
		('Panasonic-lumix','Panasonic-lumix'),
		('Tamron','Tamron'),
		('Canon','Canon'),
		('Fujifilm','Fujifilm'),
		('Nikon','Nikon'),
		('Sigma','Sigma'),
		('Sony','Sony'),
		('Zeiss','Zeiss'),)
	ETAT = (
        ('neuf sous emballage','neuf sous emballage'),
        ('neuf jamais utilisé','neuf jamais utilisé'),
        ('bon état','bon état'),
        ('moyen','moyen'),)
	sous_categorie = forms.ChoiceField(choices=CHOICES)
	etat = forms.ChoiceField(choices=ETAT)
	class Meta:
		model = Objectif
		fields = [
				'titre',
				'description',
				'image',
                'prix',]
