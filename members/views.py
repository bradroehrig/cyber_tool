from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def login_user(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect ('home')
        else:
            messages.success(request, ("There was an error logging in, trying again..."))
            return redirect ('login')

    else:
        return render(request, 'authenticate/login.html', {})

def home(request):
    return render(request, "home.html")

def logout_user(request):
    logout(request)
    messages.success(request, ("You are now logged out"))


def register_user(request):
    return render (request, 'authenticate/register_user.html', {})