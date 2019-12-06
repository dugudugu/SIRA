from django.shortcuts import render

# Render view for Why Spain Rescue Dogs page
def why_spain(request):
    return render(request, "why-spain.html" )

# Render view for SIRA Team page
def sira_team(request):
    return render(request, "sira-team.html" )
