from django import forms
from .models import Adoptable

class DogForm(forms.ModelForm):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    age = forms.CharField()
    breed = forms.CharField()
    sex = forms.CharField()
    size =forms.CharField()
    situation = forms.CharField()
    status = forms.BooleanField(label='For adoption')
    date_of_birth = forms.CharField()
    in_shelter_from = forms.CharField()
    location = forms.CharField()
    
    
    class Meta:
        model = Adoptable
        fields = ['name', 
                    'description', 
                    'age', 
                    'breed', 
                    'sex', 
                    'size', 
                    'situation', 
                    'status', 
                    'date_of_birth', 
                    'in_shelter_from', 
                    'location',
                    'dog_image1',
                    'dog_image2',
                    'dog_image3',
                    'dog_image4',]
    