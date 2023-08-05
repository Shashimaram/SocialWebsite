from django import forms
from .models import Image

class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title','url','description')
        widgets = {
            'url': forms.HiddenInput
        }
    
    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extension=['jpg', 'jpeg', 'png']
        extension = url.rsplit('.',1)[1].lower()
        if extension not in valid_extension:
            raise forms.ValidationError('the given url does not match the extension')
        return url