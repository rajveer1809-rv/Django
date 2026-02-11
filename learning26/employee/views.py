from django.http import HttpResponse
from django.shortcuts import render
from .forms import EmployeeForm, course1Form, schoolForm, gamesForm
from .models import Employee


def employeeList(request):
    employees = Employee.objects.all()
    return render(request, "employee/employeeList.html", {"employees": employees})


def employeeFilter(request):
    context = {
        "query1": Employee.objects.filter(name="raj"),
        "query2": Employee.objects.filter(post="Developer"),
        "query3": Employee.objects.filter(name="raja", post="Developer"),
        "query4": Employee.objects.filter(age__gt=23),
        "query5": Employee.objects.filter(age__gte=23),
        "query6": Employee.objects.filter(post__exact="Developer"),
        "query7": Employee.objects.filter(post__iexact="developer"),
        "query8": Employee.objects.filter(name__contains="r"),
        "query9": Employee.objects.filter(name__icontains="R"),
        "query10": Employee.objects.filter(name__startswith="R"),
        "query11": Employee.objects.filter(name__endswith="R"),
        "query12": Employee.objects.filter(name__istartswith="R"),
        "query13": Employee.objects.filter(name__iendswith="R"),
        "query14": Employee.objects.filter(name__in=["raj", "jay"]),
        "query15": Employee.objects.filter(age__range=[24, 30]),
        "query16": Employee.objects.order_by("age"),
        "query17": Employee.objects.order_by("-age"),
        "query18": Employee.objects.order_by("-salary"),
    }

    return render(request, "employee/employeeFilter.html", context)


def employeeFormView(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Employee created successfully")
    else:
        form = EmployeeForm()

    return render(request, "employee/employeeForm.html", {"form": form})


def course1FormView(request):
    if request.method == "POST":
        form = course1Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Course created successfully")
    else:
        form = course1Form()

    return render(request, "employee/course1Form.html", {"form": form})


def schoolFormView(request):
    if request.method == "POST":
        form = schoolForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("School created successfully")
    else:
        form = schoolForm()

    return render(request, "employee/schoolForm.html", {"form": form})


def gamesFormView(request):
    if request.method == "POST":
        form = gamesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Game created successfully")
    else:
        form = gamesForm()

    return render(request, "employee/gamesForm.html", {"form": form})
