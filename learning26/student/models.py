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