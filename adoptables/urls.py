from django.conf.urls import url, include
from .views import DogListView, DogDetailView, AddNewDogView


urlpatterns = [
    url(r'^$', DogListView.as_view(), name='all_dogs'),
    url(r'^(?P<pk>[0-9]+)/$', DogDetailView.as_view(), name='dog_details'),
    url(r'^new', AddNewDogView.as_view(), name='add_dog'),
    
]