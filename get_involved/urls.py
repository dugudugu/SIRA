from django.conf.urls import url, include
from .views import adoption, volunteer, faqs

urlpatterns = [
    url(r'^adoption/', adoption, name='adoption'),
    url(r'^volunteer/', volunteer, name='volunteer'),
    url(r'^FAQs/', faqs, name='faqs'),
]