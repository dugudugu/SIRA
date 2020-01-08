from django.conf.urls import url, include
from .views import all_dogs

urlpatterns = [
    url(r'^all_dogs', all_dogs, name='adoptables'),
]