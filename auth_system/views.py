from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from auth_system.forms import CustomUserCreationForm, EmailChangeForm, PhoneNumberChangeForm, CustomPasswordChangeForm


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("account")
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
                return redirect("account")
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
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def get_account(request):
    user = request.user
    context = {
        'user': user,
    }
    
    return render(
        request,
        "auth_system/account.html",
        context
    )


@login_required
def change_info(request):
    if request.method == "POST":
        return HttpResponse('Bad request', 404)
    
    user = request.user
    context = {
        'email_form': EmailChangeForm(),
        'phone_form': PhoneNumberChangeForm(),
        'password_form': CustomPasswordChangeForm(user),
    }
    
    return render(
        request,
        template_name="auth_system/change_info.html",
        context=context
    )


@login_required
def change_email(request):
    form = EmailChangeForm(request.POST, instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('account')
    return redirect('change_account_info')


@login_required
def change_phone_number(request):
    form = PhoneNumberChangeForm(request.POST, instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('account')
    return redirect('change_account_info')


@login_required
def change_password(request):
    user = request.user
    form = CustomPasswordChangeForm(user, data=request.POST)
    if form.is_valid():
        form.save()
        update_session_auth_hash(request, form.user)
        return redirect('account')
    return redirect('change_account_info')