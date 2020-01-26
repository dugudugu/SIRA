from django.conf.urls import url, include
from .views import DogListView, DogDetailView, AddNewDogView, DogUpdateView, DogDeleteView


urlpatterns = [
    url(r'^$', DogListView.as_view(), name='all_dogs'),
    url(r'^(?P<pk>[0-9]+)/$', DogDetailView.as_view(), name='dog_details'),
    url(r'^new/$', AddNewDogView.as_view(), name='add_dog'),
    url(r'^(?P<pk>[0-9]+)/update/$', DogUpdateView.as_view(), name='dog_update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', DogDeleteView.as_view(), name='dog_delete'),
]