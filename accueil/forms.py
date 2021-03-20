from django import forms
from accounts.models import User,Photographe
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import Project

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email','image','tel','bio','domaines')



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Photographe
        fields = ['camera',]

class ProjectForm(forms.Form):
	project = forms.CharField()

	class Meta:
		model = Project
		fields = [
                'titre'
				'description',
				'image',]
