from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from .models import *
from .models import Profile
from .forms import RegisterForm


# Create your views here.

def main(request):
    return render(request, 'index.html')


def about_us(request):
    return render(request, 'about.html')


def contect_us(request):
    return render(request, 'contect.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)

        if user is None:
            # Try to authenticate by email (case-insensitive)
            User = get_user_model()
            try:
                user_obj = User.objects.get(email__iexact=username)
                user = authenticate(request, username=user_obj.get_username(), password=password)
            except User.DoesNotExist:
                user = None

        if user is not None:
            login(request, user)
            # ensure a Profile record exists for this user
            try:
                Profile.objects.get_or_create(
                    user=user,
                    defaults={
                        'first_name': getattr(user, 'first_name', ''),
                        'last_name': getattr(user, 'last_name', ''),
                        'email': getattr(user, 'email', ''),
                    }
                )
            except Exception:
                pass

            messages.success(request, 'Successfully signed in.')
            return redirect('name')
        else:
            messages.error(request, 'Invalid username/email or password.')

    return render(request, 'login.html')

def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # create Profile (avoid storing raw password)
            try:
                Profile.objects.get_or_create(
                    user=user,
                    defaults={
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'email': user.email,
                    }
                )
            except Exception:
                pass

            messages.success(request, 'Registration successful. Please sign in.')
            return redirect('login_page')
    else:
        form = RegisterForm()
        
    return render(request, 'register.html', {'form': form})