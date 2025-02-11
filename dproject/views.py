from django.shortcuts import render, get_object_or_404
from .models import Project
from django.contrib.auth.decorators import login_required

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'project_detail.html', {'project': project})

def project_list(request):
    projects = Project.objects.all()  # Sab projects le aayein
    return render(request, 'project_list.html', {'projects': projects})

@login_required
def add_project(request):
    return render(request, 'add_project.html')