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
    projects = Project.objects.all() # get all projects
    context = {
        'project': project_detail,
        'projects': projects, # add projects to the context dictionary
    }
    return render(request, 'projects/detail.html', context)

def project_list(request):
    projects = Project.objects.order_by('-created_at')
    return render(request, 'project_list.html', {'projects': projects})