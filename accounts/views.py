from django.shortcuts import render, redirect, reverse
from django.contrib import auth



# View to display the index page
def index(request):
    return render(request, 'index.html')
    
# View to log user out
def logout(request):
    auth.logout(request)
    message.success(request, "You have been Logged Out!")
    return redirect(reverse('index'))
    
    