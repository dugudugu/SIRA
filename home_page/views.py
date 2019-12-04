from django.shortcuts import render, HttpResponse

# Renders home page
def homepage(request):
    return  render(request, 'index.html')