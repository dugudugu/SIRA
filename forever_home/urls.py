from django.conf.urls import url
from .views import HappyEndingListView, HappyEndingCreateView, HappyEndingUpdateView


urlpatterns = [
    url(r'^$', HappyEndingListView.as_view(), name='happy_endings'),
    url(r'^new/$', HappyEndingCreateView.as_view(), name='new_happy_ending'),
    url(r'^(?P<pk>[0-9]+)/update/$', HappyEndingUpdateView.as_view(), name='update_happy_ending'),
]