from django import forms
from .models import Banner, HomeImage

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['banner1', 'banner2', 'banner3']
        
class HomeImageForm(forms.ModelForm):
    class Meta:
        model = HomeImage
        fields = ['open_image']