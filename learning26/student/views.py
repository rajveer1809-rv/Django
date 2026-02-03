from django.shortcuts import render

def studentmarks(request):
    student_data = {
        'name': 'John Doe',
        'marks': {
            'Math': 85,
            'Science': 90,
            'History': 78,
            'English': 88
        }
    }
    return render(request, 'student/studentmarks.html', {'student': student_data})

def studentaddress(request):
    address_data = {
        'name': 'John Doe',
        'address': '123 Main Street, Cityville, State 12345'
    }
    return render(request, 'student/studentaddress.html', {'address': address_data})

def studentcontact(request):
    contact_data = {
        'name': 'John Doe',
        'contact': {
            'email': 'john.doe@example.com',
            'phone': '123-456-7890'}
    }
    return render(request, 'student/studentcontact.html', {'contact': contact_data})