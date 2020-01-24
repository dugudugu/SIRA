from django import forms
from .models import Adoptable

class DogForm(forms.ModelForm):
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