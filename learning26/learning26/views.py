"""Views for the learning26 Django app."""

from django.http import HttpResponse
from django.shortcuts import render


def test(_request):
    """Simple test view returning a plain response."""
    return HttpResponse("Hello")

def home(request):
    """Render the home page."""
    return render(request, "home.html")

def about_us(request):
    """Render the About Us page."""
    return render(request, "aboutus.html")

def contact_us(request):
    """Render the Contact Us page."""
    return render(request, "contactus.html")

def movie(request):
    """Render the Movies page."""
    return render(request, "movies.html")

def news(request):
    """Render the News page."""
    return render(request, "news.html")

def show(request):
    """Render the Show page."""
    return render(request, "show.html")

def recipe(request):
    """Render a recipe with ingredients and metadata."""
    ingredients = ["Noodles", "Sauce", "Vegetables"]
    data = {
        "name": "Noodles",
        "time": "15 mins",
        "ingredients": ingredients,
    }
    return render(request, "recipe.html", data)

def team(request):
    """Render the team page with player list and club info."""
    members = [
        "salt",
        "kohli",
        "paddikal",
        "rajat",
        "jitesh",
        "mayank",
        "tim",
        "romario",
        "krunal",
        "livingstone",
        "suyansh",
        "jacob",
    ]
    rcb = {
        "name": "royal chalangers bangaluru",
        "trophy": 1,
        "team": members,
        "captain": "rajat patidar",
    }
    return render(request, "team.html", rcb)

def car(request):
    """Render the car page with car list and metadata."""
    cars = [
        "creata",
        "verna",
        "i20",
        "venue",
        "tucson",
        "sonata",
        "alcazar",
        "aura",
    ]
    data = {
        "brand": "hundai",
        "model": "creata",
        "car": cars,
        "price": 2000000,
    }
    return render(request, "car.html", data)
