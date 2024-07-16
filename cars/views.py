from django.shortcuts import render,redirect,get_object_or_404
from cars.models import *
from cars.forms import *

def car(request):
    car = Cars.objects.all()
    car_form = CarsModelForm()
    if request.method=="POST":
        car_form = CarsModelForm(request.POST)
        if car_form.is_valid():
            car_form.save()
        return redirect("car")
    data = {
        "car" : car,
        "car_form" : car_form,
    }
    return render(request,'car/car.html',data)

def car_update(request,pk=None):
    car = get_object_or_404(Cars,pk=pk)
    if request.method=="POST":
        park_form = CarsModelForm(request.POST,instance=car)
        if park_form.is_valid():
            park_form.save()
            return redirect("car")
    car_form = CarsModelForm(instance=car)
    cars = Cars.objects.all()
    data = {
        "car":car,
        "car_form" : car_form,
    }
    return render(request,'car/car_update.html',data)

def car_delete(request,pk=None):
    car = get_object_or_404(Cars,pk=pk)
    car.delete()
    return redirect("car")

def space(request):
    space = Space.objects.all()
    space_form = SpaceModelForm()
    if request.method=="POST":
        space_form = SpaceModelForm(request.POST)
        if space_form.is_valid():
            space_form.save()
        return redirect("space")
    data = {
        "spaces" : space,
        "space_form" : space_form,
    }
    return render(request,'space/space.html',data)

def space_update(request,pk=None):
    space = get_object_or_404(Space,pk=pk)
    if request.method=="POST":
        space_form = SpaceModelForm(request.POST,instance=space)
        if space_form.is_valid():
            space_form.save()
            return redirect("space")
    space_form = SpaceModelForm(instance=space)
    space = Space.objects.all()
    data = {
        "spaces":space,
        "space_form" : space_form,
    }
    return render(request,'space/space_update.html',data)

def space_delete(request,pk=None):
    space = get_object_or_404(Space,pk=pk)
    space.delete()
    return redirect("space")

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
    return render(request,'park/park.html',data)

def park_update(request,pk=None):
    park = get_object_or_404(ParkSlot,pk=pk)
    if request.method=="POST":
        park_form = ParkModelForm(request.POST,instance=park)
        if park_form.is_valid():
            park_form.save()
            return redirect("/")
    park_form = ParkModelForm(instance=park)
    park_slot = ParkSlot.objects.all()
    data = {
        "park_slot":park_slot,
        "park_form" : park_form,
    }
    return render(request,'park/park_update.html',data)

def park_delete(request,pk=None):
    park = get_object_or_404(ParkSlot,pk=pk)
    park.delete()
    return redirect("/")

