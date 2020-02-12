from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from .views import register
from . import urls_reset


urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    url(r'^password-reset/', include(urls_reset)),
]