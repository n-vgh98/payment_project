from django.shortcuts import render, redirect
from django.core.cache import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *


def user_login(request):
    # if request.user.is_anonymous:
    if request.method == "GET":
        return render(request, 'users/login.html')
    elif request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        # if user is None:
        #     return redirect('login')
        login(request, user)

@login_required
def user_logout(request):
    pass
    logout(request)
    return redirect('login')
