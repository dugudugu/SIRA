from django.conf.urls import url, include
from .views import register
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from . import urls_reset


urlpatterns = [
    url(r'^register/$', register, name='register'),
]