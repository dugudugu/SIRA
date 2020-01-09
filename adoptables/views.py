from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Adoptable

# Views for all dogs
def all_dogs(request):
    dogs = Adoptable.objects.all()
    return render(request, "adoptable.html", {"dogs": dogs})


def dog_detail_view(request):
    obj = get_object_or_404(Adoptable, id=id)
    context = {
        "object": obj
    }
    return render(request, "dog-listing.html", context)




# View for an individual dog
# class dog_listing(DetailView):
  #   model = Adoptable
#     template_name = "dog-listing.html"
  #   context_object_name = "dog"
    # extra_context = {}
    
#     def get_object(self, queryset=Adoptable):
  #       _id = self.kwargs.get('pk')
    #     instance = get_object_or_404(Adoptable, id=_id)
      #   return instance
    

