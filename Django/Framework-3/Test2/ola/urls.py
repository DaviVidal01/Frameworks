from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="verification"),
    path("teste/",views.hof,name="index")
]