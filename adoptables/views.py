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
class DogView(TemplateView):
    template_name = "new-dog.html"
    
    def get(self, request):
        form = DogForm()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = DogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            breed = form.cleaned_data['breed']
            sex = form.cleaned_data['sex']
            size = form.cleaned_data['size']
            situation = form.cleaned_data['situation']
            status = form.cleaned_data['status']
            date_of_birth = form.cleaned_data['date_of_birth']
            in_shelter_from = form.cleaned_data['in_shelter_from']
            description = form.cleaned_data['description']
            dog_image1 = form.cleaned_data['dog_image1']
            dog_image2 = form.cleaned_data['dog_image2']
            dog_image3 = form.cleaned_data['dog_image3']
            dog_image4 = form.cleaned_data['dog_image4']
            
            return redirect ('all_dogs')
            
        args = {
                'name': name,
                'age': age,
                'breed': breed,
                'sex': sex,
                'size': size,
                'situation': situation,
                'status': status,
                'date_of_birth': date_of_birth,
                'in_shelter_from': in_shelter_from,
                'description': description,
                'dog_image1': dog_image1,
                'dog_image2': dog_image2,
                'dog_image3': dog_image3,
                'dog_image4': dog_image4,
        }
        return render(request, self.template_name, args)
