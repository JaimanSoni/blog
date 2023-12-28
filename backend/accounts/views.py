from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as user_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if User.objects.filter(email = email).exists():
            messages.error(request, "User already registered")
            return redirect("/register")
        else:
            if password1 == password2:
                new_user = User.objects.create_user(
                    first_name = first_name,
                    last_name = last_name,
                    email = email,
                    username = email,
                )
                new_user.set_password(password1)
                new_user.save()
            return redirect('/login')
    return render(request, "files/register.html")

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not User.objects.filter(email = email).exists():
            messages.error(request, "Invalid Email")
            return redirect("/login")
        
        user = authenticate(username = email , password = password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect("/login")
        else:
            user_login(request, user)
            return redirect("/home")
    return render(request, "files/login.html")

def logout_user(request):
    logout(request)
    return redirect("/home")   


def account(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        # if request.user.email != User.objects.get(email = email) and User.objects.filter(email = email).exists():
        #     messages.error(request, "User with this email id exists")
        #     return redirect("/account")

        user = User.objects.get(email = email)
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return redirect("/account")
    return render(request, "files/account.html", context= {"user" : request.user})