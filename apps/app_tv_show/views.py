from django.shortcuts import render, redirect
from apps.app_tv_show.models import *
from django.contrib import messages
# Create your views here.

def new(request):
    return render(request, "create.html")

def create(request):
    errors = Show.objects.basic_validation(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/new")
    else :
        newshow = Show.objects.create(title=request.POST['title'], network=request.POST['net'] \
            ,release_date=request.POST['date'], description=request.POST['desc'])
        return redirect("/shows/"+str(newshow.id))

def readA(request):
    context = {
        "all_shows": Show.objects.all()
    }
    return render(request, "readA.html", context)

def edit(request, num):
    context = {
        "show": Show.objects.get(id=num)
    }
    return render(request, "update.html", context)

def update(request, num):
    errors = Show.objects.basic_validation(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/"+num+"/edit")
    else :
        up = Show.objects.get(id=num)
        up.title=request.POST['title']
        up.network=request.POST['net']
        up.release_date=request.POST['date']
        up.description=request.POST['desc']
        up.save()
        return redirect("/shows/"+num)

def readO(request, num):
    context = {
        "show": Show.objects.get(id=num),
    }
    return render(request, "readO.html", context)

def delete(request, num):
    d = Show.objects.get(id=num)
    d.delete()
    return redirect("/shows")