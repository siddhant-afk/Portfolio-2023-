from django.shortcuts import render
from .models import Project
# Create your views here.


def home(request):
    projects = Project.objects.all()[::-1]
    return render(request,"projects/index.html",{'projects' : projects})