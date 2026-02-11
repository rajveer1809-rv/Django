from django.shortcuts import render
from .models import Employee


def employeeList(request):
    # select * from employee
    employees = Employee.objects.all().values()
    print(employees)
    return render(request, "employee/employeeList.html", {"employees": employees})


def employeeFilter(request):
    # where name = "raj"
    employee = Employee.objects.filter(name="raj").values()

    # where post = "Developer"
    employee2 = Employee.objects.filter(post="Developer").values()

    # where name = "raja" and post = "Developer"
    employee3 = Employee.objects.filter(name="raja", post="Developer").values()

    # age queries
    employee4 = Employee.objects.filter(age__gt=23).values()
    employee5 = Employee.objects.filter(age__gte=23).values()

    # string queries
    employee6 = Employee.objects.filter(post__exact="Developer").values()
    employee7 = Employee.objects.filter(post__iexact="developer").values()

    # contains
    employee8 = Employee.objects.filter(name__contains="r").values()
    employee9 = Employee.objects.filter(name__icontains="R").values()

    # startswith / endswith
    employee10 = Employee.objects.filter(name__startswith="R").values()
    employee11 = Employee.objects.filter(name__endswith="R").values()
    employee12 = Employee.objects.filter(name__istartswith="R").values()
    employee13 = Employee.objects.filter(name__iendswith="R").values()

    # IN query
    employee14 = Employee.objects.filter(name__in=["raj", "jay"]).values()

    # range
    employee15 = Employee.objects.filter(age__range=[24, 30]).values()

    # order by
    employee16 = Employee.objects.order_by("age").values()
    employee17 = Employee.objects.order_by("-age").values()
    employee18 = Employee.objects.order_by("-salary").values()

    # printing results
    print("query1:", employee)
    print("query2:", employee2)
    print("query3:", employee3)
    print("query4:", employee4)
    print("query5:", employee5)
    print("query6:", employee6)
    print("query7:", employee7)
    print("query8:", employee8)
    print("query9:", employee9)
    print("query10:", employee10)
    print("query11:", employee11)
    print("query12:", employee12)
    print("query13:", employee13)
    print("query14:", employee14)
    print("query15:", employee15)
    print("query16:", employee16)
    print("query17:", employee17)
    print("query18:", employee18)

    return render(request, "employee/employeeFilter.html")
