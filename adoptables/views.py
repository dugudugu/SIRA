from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, TemplateView
from .models import Adoptable
from .forms import DogForm
from .filters import DogsFilter

    
# Views for all dogs
class DogListView(ListView):
    model = Adoptable
    context_object_name = 'dogs'
    paginate_by = 8
    template_name = 'adoptable.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = DogsFilter(self.request.GET, queryset=self.get_queryset())
        return context





# View for dog details
class DogDetailView(DetailView):
    model = Adoptable
    template_name = 'dog-listing.html'


# Authenticated User Views
# View for posting new adoptable dog
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
        
# View for updating an exsisting adoptable dog
class DogUpdateView(UpdateView):
    model = Adoptable
    form_class = DogForm
    template_name = "new-dog.html"

# View for deleting an exsisting adoptable dog
class DogDeleteView(DeleteView):
    model = Adoptable
    template_name = "dog-confirm-delete.html"
    success_url = '/'