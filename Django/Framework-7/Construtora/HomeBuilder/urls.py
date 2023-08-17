from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name="index"),
    path('blogs/', views.blogs, name="blogs"),
    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),
    path('main/', views.main, name="main"),
    path('team/', views.team, name="team"),
    path('project/', views.project, name="project"),
    path('about/', views.about, name="about"),
]