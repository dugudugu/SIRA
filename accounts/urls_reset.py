from django.conf.urls import url
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    url(r'^done/$', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    url(r'^complete/$', auth_views.PasswordResetView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]