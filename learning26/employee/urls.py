from django.urls import path
from . import views

urlpatterns = [
    path("employeeList/", views.employeeList, name="employeeList"),
    path("employeeFilter/", views.employeeFilter, name="employeeFilter"),
    path("employeeForm/", views.employeeFormView, name="employeeForm"),
    path("course1Form/", views.course1FormView, name="course1Form"),
    path("schoolForm/", views.schoolFormView, name="schoolForm"),
    path("gamesForm/", views.gamesFormView, name="gamesForm"),
    path("employeeDelete/<int:id>/", views.employeeDelete, name="employeeDelete"),
    path("filterEmployee/", views.filterEmployee, name="filterEmployee"),
    path("sortEmployee/<int:id>/", views.sortEmployee, name="sortEmployee"),
    path("updateEmployee/<int:id>/", views.updateEmployee, name="updateEmployee"),
]
