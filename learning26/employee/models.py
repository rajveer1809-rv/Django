from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()
    join_date = models.DateField(auto_now_add=True)
    post = models.CharField(max_length=100)

    class Meta:
        db_table = "employee"

    def __str__(self):
        return str(self.name)


class course1(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    fees = models.IntegerField()

    class Meta:
        db_table = "course1"

    def __str__(self):
        return str(self.name)


class school(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()

    class Meta:
        db_table = "school"

    def __str__(self):
        return str(self.name)


class games(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    players = models.IntegerField()

    class Meta:
        db_table = "games"

    def __str__(self):
        return str(self.name)
