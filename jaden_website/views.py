from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


# Create your views here.

x_date = datetime.now()
currentDate = x_date.strftime("%B %d, %Y")

def index(request):
    return render(request, 'index.html', {'currentDate': currentDate})


def blog(request):
    return render(request, 'blog.html', {'currentDate': currentDate})


def projects(request):
    return render(request, 'projects.html')
