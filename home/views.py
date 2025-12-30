from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth import get_user_model
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .forms import ContactQueryForm

# <--------------------------------------------------------->User model<----------------------------------------------------------------->

User = get_user_model()

# <--------------------------------------------------------->Main page<----------------------------------------------------------------->

@login_required(login_url='login_page')
def main(request):
    return render(request, 'index.html')

# <--------------------------------------------------------->About Us page<----------------------------------------------------------------->

@login_required(login_url='login_page')
def about_us(request):
    return render(request, 'about.html')

# <--------------------------------------------------------->Contact Us page<------------------------------------------------------------->

@login_required(login_url='login_page')
def contact_us(request):
    if request.method == "POST":
        form = ContactQueryForm(request.POST)

        if form.is_valid():
            contact_query = form.save(commit=False)
            contact_query.user = request.user 
            print(contact_query.user)
            print(contact_query.subject)
            print(contact_query.message)
            contact_query.save()

            messages.success(request, "Your message has been sent successfully.")
            return redirect('contact_us')

        else:
            messages.error(request, "Please correct the errors below.")

    else:
        form = ContactQueryForm()

    return render(request, 'contact.html', {'form': form})


# <--------------------------------------------------------->Login page<----------------------------------------------------------------->

def login_page(request):
    if request.method == "POST" :
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(request, username = username, password = password)

        if user is None :
            try :
                user_obj = User.objects.get(email__iexact = username)
                user = authenticate(request, username = user_obj.get_username(), password = password)
            except User.DoesNotExist :
                messages.error(request, 'Username not found, Try to register first')
                user = None 
        if user is not None :
            login(request, user)
            messages.success(request, 'Logged in successfuly!')
            return redirect('name')
        else :
            messages.error(request,'Something went wrong, Try again')
    return render(request, 'login.html')


# <--------------------------------------------------------->Register page<----------------------------------------------------------------->

def register_page(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. Please login.")
            return redirect('login_page')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form}) 


# <--------------------------------------------------------->Logout page<----------------------------------------------------------------->

def logout_page(request) :
    logout(request)
    messages.success(request, 'Logged out successfuly')
    return redirect('name')

        