from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request, 'projects/home.html', {'projects': projects})

def contact(request):
    projects = Project.objects.all()
    return render(request, 'projects/contact.html', {'projects': projects})

def detail(request, project_id):
    project_detail = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/detail.html', {'project':project_detail})

def project_list(request):
    projects = Project.objects.order_by('-created_at')
    return render(request, 'project_list.html', {'projects': projects})