from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.
def home(request):
    return render(request, 'home.html')