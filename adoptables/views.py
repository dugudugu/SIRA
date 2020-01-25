from django.views.generic import TemplateView, UpdateView
from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import Adoptable
from .forms import DogForm

    
# Views for all dogs
class DogListView(ListView):
    model = Adoptable
    template_name = 'adoptable.html'
    context_object_name = 'dogs'


# View for dog details
class DogDetailView(DetailView):
    model = Adoptable
    template_name = 'dog-listing.html'




# Admin view for posting new adoptable dogs

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