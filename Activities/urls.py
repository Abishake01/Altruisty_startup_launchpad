from django.urls import path
from . import views

urlpatterns=[
    path('add_costquestions/',views.add_costquestions, name="costquestions"),
]