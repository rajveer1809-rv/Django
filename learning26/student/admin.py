from django.contrib import admin
from .models import (
    Student,
    StudentDetail,
    Employee1,
    Employeedetail,
)

admin.site.register(Student)
admin.site.register(StudentDetail)
admin.site.register(Employee1)
admin.site.register(Employeedetail)
