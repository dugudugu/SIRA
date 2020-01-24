from django.views.generic import TemplateView
from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import DetailView
from .models import Adoptable
from .forms import DogForm

# Views for all dogs
def all_dogs(request):
    dogs = Adoptable.objects.all()
    return render(request, "adoptable.html", {'dogs': dogs})

# View for dog details
def dog_detail_view(request, id):
    obj = get_object_or_404(Adoptable, id=id)
    context = {
        "object": obj
    }
    return render(request, "dog-listing.html", context)


# Admin view posting new adoptable dogs
class AddNewDogView(TemplateView):
    template_name = "new-dog.html"
    
    def get(self, request):
        form = DogForm()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        NewDogForm = DogForm(request.POST, request.FILES)
        if NewDogForm.is_valid():
            NewDog = NewDogForm.save()
            
            return redirect ('all_dogs')
            
        return render(request, self.template_name)
