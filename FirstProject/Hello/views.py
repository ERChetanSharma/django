from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return render(request,"home.html")
# Create your views here.

def A(request):
    return render(request,"about.html")
