from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from auth_system.forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("hotels")
    else:
        form = CustomUserCreationForm()
        
    return render(
        request, 
        template_name='auth_system/register.html',
        context = {'form': form}
    )


def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("hotels")
            else:
                messages.error(request, 'Wrong login info')
    else:
        form = AuthenticationForm()
    
    return render(
        request, 
        template_name='auth_system/login.html',
        context = {'form': form}
    )

@login_required
def log_out(request):
    logout(request)
    return redirect('hotels')
