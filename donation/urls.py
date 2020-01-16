from django.conf.urls import url
from .views import donation

urlpatterns = [
    url(r'^donate/', donation, name='donate'),
]