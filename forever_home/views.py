from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .models import HappyEnding
from .forms import HappyEndingForm


# Create your views here.
class HappyEndingListView(ListView):
    model = HappyEnding
    template_name = "happy-endings.html"
    context_object_name = 'dogs'

# Authenticated User Views
# View for posting new dog that has been adopted
class HappyEndingCreateView(CreateView):
    model = HappyEnding
    form_class = HappyEndingForm
    template_name = "new-happy-ending.html"
    success_url = reverse_lazy('happy_endings')

# View for updating a dog that has been adoipted   
class HappyEndingUpdateView(UpdateView):
    model = HappyEnding
    form_class = HappyEndingForm
    template_name = "new-happy-ending.html"
    success_url = reverse_lazy('happy_endings')