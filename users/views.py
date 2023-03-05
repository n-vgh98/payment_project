from django.shortcuts import render, redirect
from django.core.cache import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *

