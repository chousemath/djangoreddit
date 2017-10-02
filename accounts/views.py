from typing import Dict
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password_confirmation']:
            try:
              user = User.objects.get(username=request.POST['username'])
              # user = User.objects.get(email=request.POST['email'])
              return render(request, 'accounts/signup.html', create_response(False, 'Username already taken.'))
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    email=request.POST['email'],
                    password=request.POST['password']
                )
                login(request, user)
                return render(request, 'accounts/signup.html', {
                    'ok': True,
                    'message': 'Welcome to the website!'
                })
        else:
            return render(request, 'accounts/signup.html', create_response(False, 'Password and password confirmation do not match.'))
    else:
        return render(request, 'accounts/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username != '' and password != '':
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST['next'])
                else:
                    return render(request, 'accounts/signin.html', create_response(True, 'Welcome back!'))
            else:
                return render(request, 'accounts/signin.html', create_response(False, 'You have not yet created an account'))
        else:
            return render(request, 'accounts/signin.html', create_response(False, 'You are missing some information'))
    else:
        return render(request, 'accounts/signin.html', {'ok': True})

def signout(request):
    logout(request)
    return render(request, 'accounts/signin.html', create_response(True, 'Signed out'))

def create_response(ok, message) -> Dict:
    return {'ok': ok, 'message': message}
