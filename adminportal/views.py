from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username atau Password tidak valid!')

    context = {}
    return render(request, 'adminportal/loginpage.html', context)


def logoutUser(request):
    logout(request)
    return redirect('adminportal')


def home(request):
    context = {}
    return render(request, 'adminportal/dashboard.html', context)
