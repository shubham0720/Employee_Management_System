from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import EmployeeDataManager
from .forms import EmployeeDataManagerForm

# Create your views here.

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User doesnt exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'User name or password does not exists')

    context = {}
    return render(request, 'baseapp/loginpage.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'baseapp/home.html')

@login_required(login_url='login')
def employeedatadisplay(request):
    data = EmployeeDataManager.objects.all()
    context = {'data':data}
    return render(request, 'baseapp/employeedisplay.html', context)

@login_required(login_url='login')
def addNewEmployee(request):
    form = EmployeeDataManagerForm()
    if request.method == "POST":
        form = EmployeeDataManagerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employeedisplay')
    context = {'form':form}
    return render(request, 'baseapp/addeditEmployee.html', context)
