# login_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout # import login and logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import get_user_model # برای دسترسی به مدل کاربر

User = get_user_model()

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page, e.g., dashboard
                return redirect('home') # Use the name 'dashboard' from urls.py
            else:
                # Return an 'invalid login' error message.
                form.add_error(None, "نام کاربری یا رمز عبور اشتباه است.")
    else:
        form = LoginForm()
    return render(request, 'login_app/login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save() # This assumes the form handles user creation
            return redirect('login') # Redirect to login page after registration
    else:
        form = UserRegistrationForm()
    return render(request, 'login_app/register.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')

@login_required # This decorator ensures only logged-in users can access dashboard
def dashboard(request):
    return render(request, 'login_app/dashboard.html')

def profile(request):
    return render(request, 'profile.html')






