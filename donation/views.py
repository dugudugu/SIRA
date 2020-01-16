from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from django.conf import settings
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET

def donation(request):
    if request.method=="POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.save()
            
            try:
                donator = stripe.Charge.create(
                    amount = request.amount * 100,
                    currency = "EUR",
                    email = request.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
                
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                
            if donator.paid:
                messages.error(request, "Thank you for your donation!")
                return redirect(reverse('home'))
                
            else:
                messages.error(request, "Unable to take your donation")
                
        else:
            print(payment_form.errors)
            messages.error(request, " We are unable to take your donation with the card you have provided")
        
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
        
    context = {
        'payment_form' : payment_form,
        'order_form' : order_form,
        'publishable' : settings.STRIPE_PUBLISHABLE
        
    }    

    return render(request, "donation.html", context)    