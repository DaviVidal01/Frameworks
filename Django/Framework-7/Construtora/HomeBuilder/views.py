from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def blogs(request):
    return render(request,'blog-single.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def main(request):
    return render(request,'main.html')

def project(request):
    return render(request,'project.html')

def team(request):
    return render(request,'team.html')