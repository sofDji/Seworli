from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from .models import (Client,User,Photographe,Entreprise,Types)
from django.utils.translation import ugettext_lazy as _

class EntrepriseSignUpForm(UserCreationForm):
    CHOICES = (
        ('01000 Adrar','01000 Adrar'),
        ('02000 Chlef','02000 Chlef'),
        ('03000 Laghouat','03000 Laghouat'),
        ('04000 Oum El Bouaghi','04000 Oum El Bouaghi'),
        ('05000 Batna','05000 Batna'),
        ('06000 Béjaïa','06000 Béjaïa'),
        ('07000 Biskra','07000 Biskra'),
        ('08000 Béchar','08000 Béchar'),
        ('09000 Blida','09000 Blida'),
        ('10000 Bouira','10000 Bouira'),
        ('11000 Tamanrasset','11000 Tamanrasset'),
        ('12000 Tébessa','12000 Tébessa'),
        ('13000 Tlemcen','13000 Tlemcen'),
        ('14000 Tiaret','14000 Tiaret'),
        ('15000 Tizi Ouzou','15000 Tizi Ouzou'),
        ('16000 Alger','16000 Alger'),
        ('17000 Djelfa','17000 Djelfa'),
        ('18000 Jijel','18000 Jijel'),
        ('19000 Sétif','19000 Sétif'),
        ('20000 Saïda','20000 Saïda'),
        ('21000 Skikda','21000 Skikda'),
        ('22000 Sidi Bel Abbès','22000 Sidi Bel Abbès'),
        ('23000 Annaba','23000 Annaba'),
        ('24000 Guelma','24000 Guelma'),
        ('25000 Constantine','25000 Constantine'),
        ('26000 Médéa','26000 Médéa'),
        ('27000 Mostaganem','27000 Mostaganem'),
        ('28000 M\'sila','28000 M\'sila'),
        ('29000 Mascara','29000 Mascara'),
        ('30000 Ouargla','30000 Ouargla'),
        ('31000 Oran','31000 Oran'),
        ('32000 El Bayadh','32000 El Bayadh'),
        ('33000 Illizi','33000 Illizi'),
        ('34000 Bordj Bou Arreridj','34000 Bordj Bou Arreridj'),
        ('35000 Boumerdès','35000 Boumerdès'),
        ('36000 El Tarf','36000 El Tarf'),
        ('37000 Tindouf','37000 Tindouf'),
        ('38000 Tissemsilt','38000 Tissemsilt'),
        ('39000 El Oued','39000 El Oued'),
        ('40000 Khenchela','40000 Khenchela'),
        ('41000 Souk Ahras','41000 Souk Ahras'),
        ('42000 Tipaza','42000 Tipaza'),
        ('43000 Mila','43000 Mila'),
        ('44000 Aïn Defla','44000 Aïn Defla'),
        ('45000 Naâma','45000 Naâma'),
        ('46000 Témouchent','46000 Témouchent'),
        ('47000 Ghardaïa','47000 Ghardaïa'),
        ('48000 Relizane','48000 Relizane'),

    )
    CHOICES1 = (
        ('ain benian','ain benian'),
        ('alger','alger'),
    )
    CHOICES2 = (
        ('bouzeriah','bouzeriah'),
        ('truc','truc'),
    )

    nom_entreprise = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    tel = forms.CharField(max_length=10)
    bio = forms.CharField(widget=forms.Textarea,required=False)
    wilaya = forms.ChoiceField(choices=CHOICES)
    commune = forms.ChoiceField(choices=CHOICES1)
    instagram = forms.URLField(max_length=255,required=False)
    facebook = forms.URLField(max_length=255,required=False)
    twitter = forms.URLField(max_length=255,required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','nom_entreprise','first_name','last_name','email','tel','bio','password1','password2','wilaya','instagram','facebook','twitter',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_entreprise = True
        if commit:
            user.save()
            entreprise = Entreprise.objects.create(user=user,nom_entreprise=user.nom_entreprise,first_name=user.first_name,last_name=user.last_name, email = user.email,tel = user.tel,bio=user.bio,instagram=user.instagram,facebook=user.facebook,twitter=user.twitter)

        return user

class PhotographeSignUpForm(UserCreationForm):
    CHOICES = (
        ('01000 Adrar','01000 Adrar'),
        ('02000 Chlef','02000 Chlef'),
        ('03000 Laghouat','03000 Laghouat'),
        ('04000 Oum El Bouaghi','04000 Oum El Bouaghi'),
        ('05000 Batna','05000 Batna'),
        ('06000 Béjaïa','06000 Béjaïa'),
        ('07000 Biskra','07000 Biskra'),
        ('08000 Béchar','08000 Béchar'),
        ('09000 Blida','09000 Blida'),
        ('10000 Bouira','10000 Bouira'),
        ('11000 Tamanrasset','11000 Tamanrasset'),
        ('12000 Tébessa','12000 Tébessa'),
        ('13000 Tlemcen','13000 Tlemcen'),
        ('14000 Tiaret','14000 Tiaret'),
        ('15000 Tizi Ouzou','15000 Tizi Ouzou'),
        ('16000 Alger','16000 Alger'),
        ('17000 Djelfa','17000 Djelfa'),
        ('18000 Jijel','18000 Jijel'),
        ('19000 Sétif','19000 Sétif'),
        ('20000 Saïda','20000 Saïda'),
        ('21000 Skikda','21000 Skikda'),
        ('22000 Sidi Bel Abbès','22000 Sidi Bel Abbès'),
        ('23000 Annaba','23000 Annaba'),
        ('24000 Guelma','24000 Guelma'),
        ('25000 Constantine','25000 Constantine'),
        ('26000 Médéa','26000 Médéa'),
        ('27000 Mostaganem','27000 Mostaganem'),
        ('28000 M\'sila','28000 M\'sila'),
        ('29000 Mascara','29000 Mascara'),
        ('30000 Ouargla','30000 Ouargla'),
        ('31000 Oran','31000 Oran'),
        ('32000 El Bayadh','32000 El Bayadh'),
        ('33000 Illizi','33000 Illizi'),
        ('34000 Bordj Bou Arreridj','34000 Bordj Bou Arreridj'),
        ('35000 Boumerdès','35000 Boumerdès'),
        ('36000 El Tarf','36000 El Tarf'),
        ('37000 Tindouf','37000 Tindouf'),
        ('38000 Tissemsilt','38000 Tissemsilt'),
        ('39000 El Oued','39000 El Oued'),
        ('40000 Khenchela','40000 Khenchela'),
        ('41000 Souk Ahras','41000 Souk Ahras'),
        ('42000 Tipaza','42000 Tipaza'),
        ('43000 Mila','43000 Mila'),
        ('44000 Aïn Defla','44000 Aïn Defla'),
        ('45000 Naâma','45000 Naâma'),
        ('46000 Témouchent','46000 Témouchent'),
        ('47000 Ghardaïa','47000 Ghardaïa'),
        ('48000 Relizane','48000 Relizane'),

    )
    domaines = forms.ModelMultipleChoiceField(
        queryset=Types.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    tel = forms.CharField(max_length=10,required=False)
    bio = forms.CharField(widget=forms.Textarea,required=False)
    wilaya = forms.ChoiceField(choices=CHOICES)
    instagram = forms.URLField(max_length=255,required=False)
    facebook = forms.URLField(max_length=255,required=False)
    twitter = forms.URLField(max_length=255,required=False)
    camera = forms.CharField(max_length = 100)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','tel','bio', 'password1', 'password2','wilaya','instagram','facebook','twitter','camera')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_photographe = True
        if commit:
            user.save()
            photographe = Photographe.objects.create(user=user, first_name = user.first_name,last_name = user.last_name,email = user.email,tel = user.tel,bio=user.bio,wilaya=user.wilaya,instagram=user.instagram,facebook=user.facebook,twitter=user.twitter,)
            photographe.domaines.add(*self.cleaned_data.get('domaines'))
            user.domaines.add(*self.cleaned_data.get('domaines'))
            user.save()
        return user


class ClientSignUpForm(UserCreationForm):
    CHOICES = (
        ('01000 Adrar','01000 Adrar'),
        ('02000 Chlef','02000 Chlef'),
        ('03000 Laghouat','03000 Laghouat'),
        ('04000 Oum El Bouaghi','04000 Oum El Bouaghi'),
        ('05000 Batna','05000 Batna'),
        ('06000 Béjaïa','06000 Béjaïa'),
        ('07000 Biskra','07000 Biskra'),
        ('08000 Béchar','08000 Béchar'),
        ('09000 Blida','09000 Blida'),
        ('10000 Bouira','10000 Bouira'),
        ('11000 Tamanrasset','11000 Tamanrasset'),
        ('12000 Tébessa','12000 Tébessa'),
        ('13000 Tlemcen','13000 Tlemcen'),
        ('14000 Tiaret','14000 Tiaret'),
        ('15000 Tizi Ouzou','15000 Tizi Ouzou'),
        ('16000 Alger','16000 Alger'),
        ('17000 Djelfa','17000 Djelfa'),
        ('18000 Jijel','18000 Jijel'),
        ('19000 Sétif','19000 Sétif'),
        ('20000 Saïda','20000 Saïda'),
        ('21000 Skikda','21000 Skikda'),
        ('22000 Sidi Bel Abbès','22000 Sidi Bel Abbès'),
        ('23000 Annaba','23000 Annaba'),
        ('24000 Guelma','24000 Guelma'),
        ('25000 Constantine','25000 Constantine'),
        ('26000 Médéa','26000 Médéa'),
        ('27000 Mostaganem','27000 Mostaganem'),
        ('28000 M\'sila','28000 M\'sila'),
        ('29000 Mascara','29000 Mascara'),
        ('30000 Ouargla','30000 Ouargla'),
        ('31000 Oran','31000 Oran'),
        ('32000 El Bayadh','32000 El Bayadh'),
        ('33000 Illizi','33000 Illizi'),
        ('34000 Bordj Bou Arreridj','34000 Bordj Bou Arreridj'),
        ('35000 Boumerdès','35000 Boumerdès'),
        ('36000 El Tarf','36000 El Tarf'),
        ('37000 Tindouf','37000 Tindouf'),
        ('38000 Tissemsilt','38000 Tissemsilt'),
        ('39000 El Oued','39000 El Oued'),
        ('40000 Khenchela','40000 Khenchela'),
        ('41000 Souk Ahras','41000 Souk Ahras'),
        ('42000 Tipaza','42000 Tipaza'),
        ('43000 Mila','43000 Mila'),
        ('44000 Aïn Defla','44000 Aïn Defla'),
        ('45000 Naâma','45000 Naâma'),
        ('46000 Témouchent','46000 Témouchent'),
        ('47000 Ghardaïa','47000 Ghardaïa'),
        ('48000 Relizane','48000 Relizane'),

    )


    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    tel = forms.CharField(max_length=10,required=False)
    wilaya = forms.ChoiceField(choices=CHOICES)
    instagram = forms.URLField(max_length=255,required=False)
    facebook = forms.URLField(max_length=255,required=False)
    twitter = forms.URLField(max_length=255,required=False)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','tel', 'password1', 'password2','wilaya','instagram','facebook','twitter', )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        user.save()
        client = Client.objects.create(user=user,first_name = user.first_name,last_name = user.last_name,email = user.email,tel = user.tel,instagram=user.instagram,facebook=user.facebook,twitter=user.twitter)
        return user




class PhotographeDomainesForm(forms.ModelForm):
    class Meta:
        model = Photographe
        fields = ('domaines', )
        widgets = {
            'domaines': forms.CheckboxSelectMultiple
        }

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = {
		'username',
		'first_name',
		'last_name',
        'image',
		}
class PhUpdateForm(forms.ModelForm):
	class Meta:
		exclude = ('user',)
