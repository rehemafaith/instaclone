from django import forms 
from .models import Image,Profile



class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ("photo_image","caption")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =("profile_photo","bio") 