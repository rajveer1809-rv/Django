# pylint: disable=missing-docstring,invalid-name,too-many-locals

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm, course1Form, schoolForm, gamesForm
from .models import Employee


def employeeList(request):
    employees = Employee.objects.all()

    print("\n--- ALL EMPLOYEES ---")
    for emp in employees:
        print(emp.id, emp.name, emp.age, emp.salary, emp.post)

    return render(request, "employee/employeeList.html", {"employees": employees})


def employeeFilter(request):
    query1 = Employee.objects.filter(name="raj")
    query2 = Employee.objects.filter(post="Developer")
    query3 = Employee.objects.filter(name="raja", post="Developer")
    query4 = Employee.objects.filter(age__gt=23)
    query5 = Employee.objects.filter(age__gte=23)
    query6 = Employee.objects.filter(post__exact="Developer")
    query7 = Employee.objects.filter(post__iexact="developer")
    query8 = Employee.objects.filter(name__contains="r")
    query9 = Employee.objects.filter(name__icontains="R")
    query10 = Employee.objects.filter(name__startswith="R")
    query11 = Employee.objects.filter(name__endswith="R")
    query12 = Employee.objects.filter(name__istartswith="R")
    query13 = Employee.objects.filter(name__iendswith="R")
    query14 = Employee.objects.filter(name__in=["raj", "jay"])
    query15 = Employee.objects.filter(age__range=[24, 30])
    query16 = Employee.objects.order_by("age")
    query17 = Employee.objects.order_by("-age")
    query18 = Employee.objects.order_by("-salary")

    queries = [
        query1, query2, query3, query4, query5, query6, query7,
        query8, query9, query10, query11, query12, query13,
        query14, query15, query16, query17, query18
    ]

    for i, q in enumerate(queries, start=1):
        print(f"\nQuery{i} result:")
        for emp in q:
            print(emp.id, emp.name, emp.age, emp.salary, emp.post)

    context = {
        "query1": query1,
        "query2": query2,
        "query3": query3,
        "query4": query4,
        "query5": query5,
        "query6": query6,
        "query7": query7,
        "query8": query8,
        "query9": query9,
        "query10": query10,
        "query11": query11,
        "query12": query12,
        "query13": query13,
        "query14": query14,
        "query15": query15,
        "query16": query16,
        "query17": query17,
        "query18": query18,
    }

    return render(request, "employee/employeeFilter.html", context)


def employeeFormView(request):
    form = EmployeeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("employeeList")

    return render(request, "employee/employeeForm.html", {"form": form})


def course1FormView(request):
    form = course1Form(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponse("Course created successfully")

    return render(request, "employee/course1Form.html", {"form": form})


def schoolFormView(request):
    form = schoolForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponse("School created successfully")

    return render(request, "employee/schoolForm.html", {"form": form})


def gamesFormView(request):
    form = gamesForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponse("Game created successfully")

    return render(request, "employee/gamesForm.html", {"form": form})


def employeeDelete(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect("employeeList")


def filterEmployee(request):
    employees = Employee.objects.filter(age__gt=25)
    return render(request, "employee/employeeList.html", {"employees": employees})


def sortEmployee(request, id):
    if id == 1:
        employees = Employee.objects.order_by("age")
    elif id == 2:
        employees = Employee.objects.order_by("-age")
    elif id == 3:
        employees = Employee.objects.order_by("salary")
    elif id == 4:
        employees = Employee.objects.order_by("-salary")
    else:
        employees = Employee.objects.all()

    return render(request, "employee/employeeList.html", {"employees": employees})


def updateEmployee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("employeeList")
    else:
        form = EmployeeForm(instance=employee)

    return render(request, "employee/updateEmployee.html", {"form": form})
