from django import forms
from .models import Post,Comment,Photo
from PIL import Image,ImageEnhance 
from django.core.files import File
 


class espaceForm(forms.Form):
	post = forms.CharField()

	class Meta:
		model = Post
		fields = [
				'content',
				'image',]

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)




class PhotoForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())
    rotate = forms.FloatField(widget=forms.HiddenInput())
    Black_and_White = forms.CharField(required=False)
    brightness = forms.FloatField(required=False)
    sharpness = forms.FloatField(required=False)
    contrast = forms.FloatField(required=False)
    class Meta:
        model = Photo
        fields = ('file', 'x', 'y', 'width', 'height','rotate','Black_and_White','brightness','sharpness','contrast', )
        widgets = {
            'file': forms.FileInput(attrs={
                'accept': 'image/*'  # this is not an actual validation! don't rely on that!
            })
        }

    def save(self):
        photo = super(PhotoForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')
        r = self.cleaned_data.get('rotate')
        bandw = self.cleaned_data.get('Black_and_White')
        bri = self.cleaned_data.get('brightness')
        sha = self.cleaned_data.get('sharpness')
        con = self.cleaned_data.get('contrast')
        wid = int(w)
        hei = int(h)
        rot = int(r)
        image = Image.open(photo.file)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((wid, hei), Image.ANTIALIAS)
        rotated_image = resized_image.rotate(-rot, resample=0, expand=0)
        bw_photo = rotated_image.convert(bandw)
        if not bri:
            enhancer = ImageEnhance.Brightness(bw_photo)
            enhanced_im = enhancer.enhance(1.0)
        else:
            enhancer = ImageEnhance.Brightness(bw_photo)
            enhanced_im = enhancer.enhance(bri)
       

        if not sha:
            enhancer2 = ImageEnhance.Sharpness(enhanced_im)
            enhanced_im2 = enhancer2.enhance(1.0)
        else:
            enhancer2 = ImageEnhance.Sharpness(enhanced_im)
            enhanced_im2 = enhancer2.enhance(sha)


        if not con:
            enhancer3 = ImageEnhance.Contrast(enhanced_im2)
            enhanced_im3 = enhancer3.enhance(1.0) 
        else:
            enhancer3 = ImageEnhance.Contrast(enhanced_im2)
            enhanced_im3 = enhancer3.enhance(con)

        enhanced_im3.save(photo.file.path)


        return photo
