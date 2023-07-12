from django.urls import path
from . import views 

urlpatterns = [
    path("",views.index,name ="index"),
    path("oi/",views.oi,name="teste"),
    path("github/",views.github,name="github"),
    path("template/",views.tema,name="template"),
    path("git/",views.git,name="git")
]
