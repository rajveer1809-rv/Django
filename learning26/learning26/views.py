from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    return HttpResponse("Hello")


def about_us(request):
    return render(request,"aboutus.html")

def contact_us(request):
    return render(request,"contactus.html")

def home(request):
    return render(request,"home.html")

def movie(request):
    return render(request,"movies.html")

def news(request):
    return render(request,"news.html")

def show(request):
    return render(request,"show.html")