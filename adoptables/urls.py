from django.conf.urls import url, include
from .views import all_dogs, dog_detail_view, DogView

urlpatterns = [
    url(r'^all_dogs', all_dogs, name='all_dogs'),
    url(r'^(?P<id>\d+)/$', dog_detail_view, name="dog_details"),
    url(r'^dog_view', DogView.as_view(), name='dog_view')
]