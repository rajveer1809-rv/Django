
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("studentmarks/", views.studentmarks),
    path("studentaddress/", views.studentaddress),
    path("studentcontact/", views.studentcontact),
]
