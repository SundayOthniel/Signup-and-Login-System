from django.shortcuts import render, redirect
from .form import SignUpForm
from .models import SignUp
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError


def home(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            form = SignUpForm()
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        username = request.POST['number']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
        else:
            error_message = 'Invalid username or password.'
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')
