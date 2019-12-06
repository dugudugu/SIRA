from django.conf.urls import url, include
from .views import why_spain, sira_team

urlpatterns = [
    url(r'^why_spain/', why_spain, name='why_spain'),
    url(r'^sira_team/', sira_team, name='sira_team'), 
]
