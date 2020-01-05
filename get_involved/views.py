from django.shortcuts import render

# Render view for Adoption info page
def adoption(request):
    return render(request, "adoption.html")

# Render view for Volunteer info page
def volunteer(request):
    return render(request, "volunteer.html")

# Render view for FAQs page
def faqs(request):
    return render(request, "faqs.html")