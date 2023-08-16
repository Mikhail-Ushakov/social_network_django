from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify

from typing import Any
import requests

from .models import ImageModel


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['title', 'url', 'description']
        widgets = {
            'url': forms.HiddenInput,
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extensions = url.rsplit('.', 1)[1].lower()
        if extensions not in valid_extensions:
            raise forms.ValidationError('Неподдерживаемое расширение')
        return url
    
    def save(self, force_insert=False, force_update=False, commit=True) -> Any:
        image_obj = super().save(commit=False)
        url_image = self.cleaned_data['url']

        extension = url_image.rsplit('.', 1)[1].lower()
        name_image = slugify(image_obj.title)
        full_name = f'{name_image}.{extension}'
        
        response = requests.get(url_image)
        image_obj.image.save(full_name, ContentFile(response.content), save=False)

        if commit:
            image_obj.save()
        return image_obj