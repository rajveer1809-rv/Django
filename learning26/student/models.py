from django.db import models


class Student(models.Model):
    studentname = models.CharField(max_length=100)
    studentage = models.IntegerField()
    studentcontect = models.CharField(max_length=15, null=True)
    studentcity = models.CharField(max_length=100)
    studentemail = models.EmailField()

    class Meta:
        db_table = "student"


class StudentDetail(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    studentaddress = models.CharField(max_length=200)
    studentqualification = models.CharField(max_length=100)
    studentexperience = models.IntegerField()

    class Meta:
        db_table = "studentdetail"


class Employee1(models.Model):
    employeename = models.CharField(max_length=100)
    employeeage = models.IntegerField()
    employeecity = models.CharField(max_length=100)
    employeeemail = models.EmailField()

    class Meta:
        db_table = "employee1"

    def __str__(self):
        return self.employeename


class Employeedetail(models.Model):
    employee = models.OneToOneField(Employee1, on_delete=models.CASCADE)
    employeeaddress = models.CharField(max_length=200)
    employeequalification = models.CharField(max_length=100)
    employeeexperience = models.IntegerField()

    class Meta:
        db_table = "employeedetail"

    def __str__(self):
        return self.employee.employeename
