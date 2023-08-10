from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def browse(request):
    return render(request, 'browse.html')

def details(request):
    return render(request, 'details.html')

def profile(request):
    return render(request, 'profile.html')

def streams(request):
    return render(request, 'streams.html')

