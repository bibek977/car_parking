from django.shortcuts import render,redirect
from cars.models import *
from cars.forms import *

def home(request):
    cars = Cars.objects.all()
    park_slot = ParkSlot.objects.all()
    car_form = CarsModelForm()
    space_form = SpaceModelForm()
    park_form = ParkModelForm()
    if request.method=="POST":
        park_form = ParkModelForm(request.POST)
        if park_form.is_valid():
            park_form.save()
        return redirect("/")
    data = {
        "cars" : cars,
        "park_slot":park_slot,
        "car_form" : car_form,
        "space_form" : space_form,
        "park_form" : park_form,
    }
    return render(request,'home.html',data)

def car(request,pk=None):
    cars = Cars.objects.all()
    car_form = CarsModelForm()
    if request.method=="POST":
        car_form = CarsModelForm(request.POST)
        if car_form.is_valid():
            car_form.save()
        return redirect("/")
    data = {
        "cars" : cars,
        "car_form" : car_form,
    }
    return render(request,'cars_modal.html',data)

def space(request):
    space = Space.objects.all()
    space_form = SpaceModelForm()
    if request.method=="POST":
        space_form = SpaceModelForm(request.POST)
        if space_form.is_valid():
            space_form.save()
        return redirect("/")
    data = {
        "spaces" : space,
        "space_form" : space_form,
    }
    return render(request,'space_modal.html',data)

def park(request):

    park_slot = ParkSlot.objects.all()

    park_form = ParkModelForm()
    if request.method=="POST":
        park_form = ParkModelForm(request.POST)
        if park_form.is_valid():
            park_form.save()
        return redirect("/")

    data = {
        "park_slot":park_slot,
        "park_form" : park_form,
    }
    return render(request,'park_modal.html',data)

