from django import forms

    
class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(widget=forms.EmailInput)
    message = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        fields = ['name', 'email', 'message',]
        widgets = {
            'name': forms.TextInput(attrs={'required': True}),
            'email': forms.EmailInput(attrs={'required': True}),
            'message': forms.TextInput(attrs={'required': True}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'input'
        self.fields['name'].widget.attrs['placeholder'] = 'Email e.g. Sam Smith'
        
        self.fields['email'].widget.attrs['class'] = 'input'   
        self.fields['email'].widget.attrs['placeholder'] = 'Email e.g. s.smith@gmail.com'
        
        self.fields['message'].widget.attrs['class'] = 'textarea'
        self.fields['message'].widget.attrs['placeholder'] = 'How can we be of help?'