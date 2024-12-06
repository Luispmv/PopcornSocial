from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('movie_catalog')
                else:
                    messages.error(request, 'Your account is disabled.')
                    return redirect('login')
            else:
                messages.error(request, 'Invalid username or password.')
                return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Verificar si el nombre de usuario o el correo electrónico ya existen
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return render(request, 'register.html', {'form': form})
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists.')
                return render(request, 'register.html', {'form': form})

            # Crear el nuevo usuario
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            # Mensaje de éxito y redirección a la página de inicio de sesión o de inicio
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')  # Cambia 'login' a la URL de tu vista de inicio de sesión

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

