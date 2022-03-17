from django.urls import path
from .views import *

urlpatterns = [
    path("all/" , get_all , name="all"),
    path("all/<str:name>" , get_instance , name= "obj"),
    path("all/<str:name>/add/<str:num>" , add_pashiz, name="add"),
    path("all/<str:name>/subtract/<str:num>" , subtract_pashiz,name="subtract"),
    path("all/<str:name>/set/<str:num>" , set_pashiz , name = "set")    
]

