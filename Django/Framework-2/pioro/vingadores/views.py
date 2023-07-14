from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>PIORO</h1>')

def app(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')