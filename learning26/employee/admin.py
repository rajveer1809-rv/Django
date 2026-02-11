from django.contrib import admin

# Register your models here.
from .models import Employee, course1, school, games
admin.site.register(Employee)
admin.site.register(course1)
admin.site.register(school)
admin.site.register(games)