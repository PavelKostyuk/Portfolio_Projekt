from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    projects = Project.objects
    return render(request, 'projects/home.html', {'projects':projects})

def about(request):
    return render(request, 'projects/about.html')