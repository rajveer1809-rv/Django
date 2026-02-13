from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm, course1Form, schoolForm, gamesForm
from .models import Employee


# ---------------- EMPLOYEE LIST ----------------
def employeeList(request):
    employees = Employee.objects.all()
    return render(request, "employee/employeeList.html", {"employees": employees})


# ---------------- EMPLOYEE FILTER DEMO ----------------
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


# ---------------- EMPLOYEE FORM ----------------
def employeeFormView(request):
    form = EmployeeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("employeeList")

    return render(request, "employee/employeeForm.html", {"form": form})


# ---------------- COURSE FORM ----------------
def course1FormView(request):
    form = course1Form(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponse("Course created successfully")

    return render(request, "employee/course1Form.html", {"form": form})


# ---------------- SCHOOL FORM ----------------
def schoolFormView(request):
    form = schoolForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponse("School created successfully")

    return render(request, "employee/schoolForm.html", {"form": form})


# ---------------- GAMES FORM ----------------
def gamesFormView(request):
    form = gamesForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponse("Game created successfully")

    return render(request, "employee/gamesForm.html", {"form": form})


# ---------------- DELETE EMPLOYEE ----------------
def employeeDelete(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect("employeeList")


# ---------------- FILTER EMPLOYEE ----------------
def filterEmployee(request):
    employees = Employee.objects.filter(age__gt=25)
    return render(request, "employee/employeeList.html", {"employees": employees})


# ---------------- SORT EMPLOYEE ----------------
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
