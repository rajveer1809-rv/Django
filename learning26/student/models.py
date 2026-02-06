from django.db import models

# Create your models here.
class Student(models.Model):
    studentname = models.CharField(max_length=100)
    studentage = models.IntegerField()
    studentcontect = models.CharField(max_length=15,null=True)
    studentcity = models.CharField(max_length=100)
    studentemail = models.EmailField()
    
    class Meta:
        db_table = 'student'

class studentdetail(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    studentaddress = models.CharField(max_length=200)
    studentqualification = models.CharField(max_length=100)
    studentexperience = models.IntegerField()
    
    class Meta:
        db_table = 'studentdetail'

class Product(models.Model):
    productname = models.CharField(max_length=100)
    productprice = models.FloatField()
    productdesc = models.TextField()
    productstatus = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'product'

class Car(models.Model):
    carname = models.CharField(max_length=100)
    carmodel = models.CharField(max_length=100)
    carcolor = models.CharField(max_length=100,null=True)
    caryear = models.IntegerField()
    
    class Meta:
        db_table = 'car'

class category(models.Model):
    categoryname = models.CharField(max_length=100)
    categorydesc = models.TextField()
    
    class Meta:
        db_table = 'category'
    def __str__(self):
        return self.categoryname

class services(models.Model):
    servicename = models.CharField(max_length=100)
    service = models.ForeignKey(category,on_delete=models.CASCADE)
    servicedesc = models.TextField()
    serviceprice = models.FloatField()
    
    class Meta:
        db_table = 'services'
    def __str__(self):
        return self.servicename

class Employee(models.Model):
    employeename = models.CharField(max_length=100)
    employeeage = models.IntegerField()
    employeecity = models.CharField(max_length=100)
    employeeemail = models.EmailField()
    
    class Meta:
        db_table = 'employee'
    def __str__(self):
        return self.employeename

class Employeedetail(models.Model):
    employee = models.OneToOneField(Employee,on_delete=models.CASCADE)
    employeeaddress = models.CharField(max_length=200)
    employeequalification = models.CharField(max_length=100)
    employeeexperience = models.IntegerField()
    
    class Meta:
        db_table = 'employeedetail'
    def __str__(self):
        return self.employee.employeename
    
class Teacher(models.Model):
    teachername = models.CharField(max_length=100)
    teacherage = models.IntegerField()
    teachercity = models.CharField(max_length=100)
    teacheremail = models.EmailField()
    
    class Meta:
        db_table = 'teacher'
    def __str__(self):
        return self.teachername

class subject(models.Model):
    subjectname = models.CharField(max_length=100)
    subjectteacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    subjectcode = models.CharField(max_length=20)
    subjectdesc = models.TextField()
    
    class Meta:
        db_table = 'subject'
    def __str__(self):
        return self.subjectname

class Book(models.Model):
    booktitle = models.CharField(max_length=200)
    bookauthor = models.CharField(max_length=100)
    bookpublisher = models.CharField(max_length=100)
    bookprice = models.FloatField()
    
    class Meta:
        db_table = 'book'
    def __str__(self):
        return self.booktitle

class LibraryMember(models.Model):
    membername = models.CharField(max_length=100)
    member = models.ForeignKey(Book,on_delete=models.CASCADE)
    memberemail = models.EmailField()
    memberphone = models.CharField(max_length=15)
    
    class Meta:
        db_table = 'librarymember'
    def __str__(self):
        return self.membername