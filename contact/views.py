from SIRA import settings
from django.core.mail import send_mail
from django.template.loader import get_template
from django.shortcuts import render, redirect

from .forms import ContactForm


def contact(request):
    template = "contact.html"
    
    if request.method == 'GET':
        form = ContactForm
        
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            form_name = form.cleaned_data['name']
            form_email = form.cleaned_data['email']
            form_message = form.cleaned_data['message']
            
            subject = 'You have recieced a new contact request'
            from_email = settings.EMAIL_HOST_USER
            to_mail =  [settings.EMAIL_HOST_USER, 'marchena.cindy@gmail.com']
            
            context ={
                'user' : form_name,
                'message' : form_message,
                'email' : form_email
            }
            
            contact_message = get_template('contact_message.txt').render(context)
            
            send_mail(subject, contact_message, from_email, to_mail,  fail_silently=True)
           
            
    form_view = {
        "form": form, 
    }    
    return render(request, "contact.html", form_view)