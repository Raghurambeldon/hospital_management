from django.shortcuts import render, redirect , get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
from appointments.models import Appointment
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # now calls django.contrib.auth.login
                messages.success(request, f"Welcome {user.first_name}!")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, "users/login.html", {"form": form})
def user_logout(request):  # ✅ renamed
    logout(request)         # now calls django.contrib.auth.logout
    messages.info(request, "You have been logged out.")
    return redirect("home")



@login_required
def dashboard(request):
    appointments = Appointment.objects.filter(user=request.user).order_by('-date', '-time')
    return render(request, 'users/dashboard.html', {'appointments': appointments})
