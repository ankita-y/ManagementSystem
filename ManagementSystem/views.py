from django.shortcuts import render, redirect
from .models import *
from .forms import * 
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def registerationpage(request):
    if request.method == "POST":
        form = RegistrationPage(request.POST)
        if form.is_valid():
            form.save()
            form = RegistrationPage()
            messages.success(request, 'Account created successfully')
    else:
        form = RegistrationPage()
    return render(request,'registerationpage.html',{'form':form})

def clientinformation(request):
    if request.method == "POST":
        form = ClientInfoForm(request.POST)
        if form.is_valid():
            form.save()
            form = ClientInfoForm()
            messages.success(request, 'Client Information updated in database successfully')
    else:
        form = ClientInfoForm()
    return render(request,'clientinformation.html',{'form':form})

def deviceinfo(request):
    if request.method == "POST":
        form = DeviceInfoForm(request.POST)
        if form.is_valid():
            form.save()
            form = DeviceInfoForm()
            messages.success(request, 'Devices information stored in database successfully')
    else:
        form = DeviceInfoForm()
    return render(request,'deviceinfo.html')