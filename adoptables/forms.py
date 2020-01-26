from django import forms
from .models import Adoptable


class DogForm(forms.ModelForm):
    class Meta:
        model = Adoptable
        fields = ['name', 'in_shelter_from', 'date_of_birth', 'age', 'size', 'sex', 'breed', 'location', 'situation', 'status', 'description', 
                    'dog_image1','dog_image2','dog_image3', 'dog_image4']
        widgets =  {
            'name' : forms.TextInput(attrs={'class': 'input', 'placeholder': 'e.g. Buddy' ,'autofocus': True, 'required': True}),
            'in_shelter_from' : forms.TextInput(attrs={'class': 'input', 'placeholder': 'YYYY/MM/DD e.g. 2019/02/25', 'required': True}),
            'date_of_birth' : forms.TextInput(attrs={'class': 'input', 'placeholder': 'YYYY/MM/DD e.g. 2019/02/25', 'required': True}),
            'age' : forms.TextInput(attrs={'class': 'input', 'placeholder': 'Dogs age e.g. 7 years old' ,'autofocus': True, 'required': True}),
            'breed' : forms.TextInput(attrs={'class': 'input', 'placeholder': 'Type of dog e.g. Mix breed, Pitbull .....' ,'autofocus': True, 'required': True}),
            'sex' : forms.Select(attrs={'class': 'input'}),
            'size' : forms.Select(attrs={'class': 'input'}),
            'situation' : forms.Select(attrs={'class': 'input'}),
            'status' : forms.NullBooleanSelect(attrs={'class': 'input'}),
            'location' : forms.Select(attrs={'class': 'input'}),
            'description' : forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Give a brief description of the rescue dog' ,'autofocus': True, 'required': True}),
        }           
