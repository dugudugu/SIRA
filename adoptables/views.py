from django.shortcuts import render
from .models import Adoptable

# Views for all dogs
def all_dogs(request):
    dogs = Adoptable.objects.all()
    return render(request, "adoptable.html", {"dogs": dogs})

# 