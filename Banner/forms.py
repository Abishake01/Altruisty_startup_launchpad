from django import forms
from .models import Banner, HomeImage , Events_update

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['banner1', 'banner2', 'banner3']
        
class HomeImageForm(forms.ModelForm):
    class Meta:
        model = HomeImage
        fields = ['college_home','intern_home']
        
class EventsForm(forms.ModelForm):
    class Meta:
        model = Events_update
        fields = ['events']