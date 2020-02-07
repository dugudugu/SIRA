from django.shortcuts import render
from adoptables.models import Adoptable


# Render view for Why Spain Rescue Dogs page
def why_spain(request):
    
    featured_dogs = Adoptable.objects.filter().order_by('?')[:6]
    context = {
        'featured_dogs': featured_dogs,
        'size': 'size',
    }
    return render(request, "why-spain.html", context )

# Render view for SIRA Team page
def sira_team(request):
    return render(request, "sira-team.html" )
