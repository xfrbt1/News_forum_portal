from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from authentication.forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout


def login_page(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'auth/login.html', context={'form': form})


def reg_page(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth_page')
    else:
        form = UserRegisterForm()
    return render(request, 'auth/registration.html', context={'form' : form})


def logout_user(request):
    logout(request)
    return redirect('home')