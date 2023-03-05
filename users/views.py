from django.shortcuts import render, redirect
from django.core.cache import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *


def user_login(request):
    if request.user.is_anonymous:
        if request.method == "GET":
            cache.set('next', request.GET.get('next', None))

            login_form = LoginForm()
            return render(request, 'users/login.html', context={'form': login_form})
        elif request.method == "POST":
            user = authenticate(request, email=request.POST.get('email'),
                                password=request.POST.get('password'))
            if user is None:
                return redirect('login')
            login(request, user)
            next_url = cache.get('next')
            if next_url:
                cache.delete('next')
                return HttpResponseRedirect(next_url)
            return HttpResponse('success')
    else:
        return HttpResponse('success')

@login_required
def user_logout(request):
    pass
    # logout(request)
    # return redirect('movies_list')