from django import forms
from .models import Donation


class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2036)]

    credit_card_number = forms.CharField(label='Credit card number')
    cvv = forms.CharField(label='Security code (CVV)')
    expiry_month = forms.ChoiceField(choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(choices=YEAR_CHOICES)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    
    class Meta:
        fields = ['credit_card_number', 'cvv', 'expiry_month', 'expiry_year', 'stripe_id']
        widget = {
            'credit_card_number': forms.TextInput(attrs={'required': True}),
            'cvv': forms.TextInput(attrs={'required': True}),
            'expiry_month': forms.Select(attrs={'required': True}),
            'expiry_year': forms.Select(attrs={'required': True}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['credit_card_number'].widget.attrs['class'] = 'input'
        self.fields['credit_card_number'].widget.attrs['placeholder'] = 'Fill in card number'
        
        self.fields['cvv'].widget.attrs['class'] = 'input'   
        self.fields['cvv'].widget.attrs['placeholder'] = 'Fill in the CVV'
        
        self.fields['expiry_month'].widget.attrs['class'] = 'input'   
        self.fields['expiry_month'].widget.attrs['placeholder'] = 'Select the cards expire month'
        
        self.fields['expiry_year'].widget.attrs['class'] = 'input'
        self.fields['expiry_year'].widget.attrs['placeholder'] = 'Select the cards expire year'

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['full_name', 'email', 'donation','country',]
        widget = {
            'full_name': forms.TextInput(attrs={'required': False}),
            'email': forms.EmailInput(attrs={'required': False}),
            'country': forms.TextInput(attrs={'required': True}),
            'donation': forms.TextInput(attrs={'required': True}),   
        } 
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs['class'] = 'input'
        self.fields['full_name'].widget.attrs['placeholder'] = 'Full name e.g. Sam Smith'
        
        self.fields['email'].widget.attrs['class'] = 'input'   
        self.fields['email'].widget.attrs['placeholder'] = 'Email e.g. s.smith@gmail.com'
        
        self.fields['country'].widget.attrs['class'] = 'input'   
        self.fields['country'].widget.attrs['placeholder'] = 'Country e.g. Netherlands'
        
        self.fields['donation'].widget.attrs['class'] = 'input'
        self.fields['donation'].widget.attrs['placeholder'] = 'How much would you like to donate'