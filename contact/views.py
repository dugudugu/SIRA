from SIRA import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .forms import ContactForm


def contact(request):
    template = "contact.html"
    
    if request.method == 'GET':
        form = ContactForm(request.GET)
        
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            form_name = form.cleaned_data['name']
            form_subject = form.cleaned_data['subject']
            form_email = form.cleaned_data['email']
            form_message = form.cleaned_data['message']
            
            subject = 'Site contact form'
            from_email = settings.EMAIL_HOST_USER
            to_mail = [from_email]
            
            contact_message ="%s: %s via %s"%(
                form_name, 
                form_message, 
                form_email)
            
            send_mail(subject, 
                form_message, 
                from_email, 
                to_mail, 
                fail_silently=True)
            
    context = {
        "form": form, 
    }    
    return render(request, "contact.html", context)
    
    
    