from django.conf.urls import url
from .views import DonationView

urlpatterns = [
    url(r'^$', DonationView, name='donate'),
]