from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm



# View to display the index page
def index(request):
    return render(request, 'index.html')
    
# View to log user out
def logout(request):
    auth.logout(request)
    messages.success(request, "You have been Logged Out!")
    return redirect(reverse('index'))
    
# View login page
def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})   