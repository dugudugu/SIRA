from django.conf.urls import url, include
from .views import adoption, volunteer, faqs, guide

urlpatterns = [
    url(r'^adoption/', adoption, name='adoption'),
    url(r'^volunteer/', volunteer, name='volunteer'),
    url(r'^FAQs/', faqs, name='faqs'),
    url(r'^guide/', guide, name='adoption-guide'),
]