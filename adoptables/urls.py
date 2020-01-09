from django.conf.urls import url, include
from .views import all_dogs, dog_detail_view

urlpatterns = [
    url(r'^all_dogs', all_dogs, name='all_dogs'),
    url(r'^Adoptable/<int:id>/', dog_detail_view, name="dog_details"),
]