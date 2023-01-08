from django.shortcuts import render
from .models import Project
import datetime as dt
# Create your views here.

today = dt.date.today()

def home(request):
    projects = Project.objects.all()[::-1]
    return render(request,"projects/index.html",{'projects' : projects,'year':today.year})