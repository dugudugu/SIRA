from django.conf.urls import url, include
from .views import RegisterUserView, LoginUserView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from . import urls_reset


urlpatterns = [
    url(r'^register/$', view=RegisterUserView.as_view(), name='register'),
    url(r'^login/$', view=LoginUserView.as_view(), name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'home'}, name='logout'),
    url(r'^password-reset/', include(urls_reset)),
]