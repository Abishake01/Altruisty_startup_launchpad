from django import forms
from .models import Banner, HomeImage

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = '__all__'
        
class HomeForm(forms.ModelForm):
    class Meta:
        model = HomeImage
        fields = '__all__'

