from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render, redirect

from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from .forms import RegisterUserForm, LoginForm


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = "register.html"
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('home')

        return super(RegisterUserView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return redirect('login')

class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = "login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')