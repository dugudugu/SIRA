from django import forms
from .models import Donation


class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2036)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    
    class Meta:
        fields = ['credit_card_number', 'cvv', 'expiry_month', 'expiry_year',]
       
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['credit_card_number'].widget.attrs['class'] = 'input'
        self.fields['credit_card_number'].widget.attrs['placeholder'] = 'Fill in card number e.q xxxx xxxx xxxx xxxx'
        
        self.fields['cvv'].widget.attrs['class'] = 'input'   
        self.fields['cvv'].widget.attrs['placeholder'] = 'Fill in the CVV. The CVV can be found at the back of your Card'
        
        self.fields['expiry_month'].widget.attrs['class'] = 'input'   
        self.fields['expiry_year'].widget.attrs['class'] = 'input'
        

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['full_name', 'email', 'donation','country',]

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