from django.shortcuts import render
from .models import Flight


def index(request):
    flights = Flight.objects.all().order_by("id")
    print(flights)

    return render(request, "flights/index.html", {
        "flights": flights
    })