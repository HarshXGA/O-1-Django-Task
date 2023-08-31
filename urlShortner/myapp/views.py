from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello_world(request):
    return HttpResponse("Hello Harsh Learning Django?")

def home_page(request):
    return render(request,"index.html")

def task_page(request):
    return render(request,"task.html")