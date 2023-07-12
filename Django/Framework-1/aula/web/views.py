from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<h2>Olá mundo.</h2>')

def oi(request):
    return HttpResponse("<p>Teste de uma segunda url</p>")

def github(request):
    return HttpResponse("<h1>DaviVidal01</h1> <p>Follow Me for More</p>")

def tema(request):
    return render(request,"index.html")

def git(request):
    return render(request,"github.html")