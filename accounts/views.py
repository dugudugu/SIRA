from django.shortcuts import render



# View to display the index page
def index(request):
    return render(request, 'index.html')