from django.shortcuts import render
# importing objects from the data base
from .models import Project

def home(request):
    # pass the objects from the database into a variable
    projects = Project.objects.all()
    # and assign it in a dictionary value for projects
    return render(request, 'portfolio/index.html', {'projects':projects})


