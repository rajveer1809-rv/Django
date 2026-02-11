from django import forms
from .models import Employee, course1, school, games

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class course1Form(forms.ModelForm):
    class Meta:
        model = course1
        fields = '__all__'

class schoolForm(forms.ModelForm):
    class Meta:
        model = school
        fields = '__all__'

class gamesForm(forms.ModelForm):
    class Meta:
        model = games
        fields = '__all__'