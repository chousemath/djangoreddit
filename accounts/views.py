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
                return render(
                    request,
                    'accounts/signup.html',
                    create_response(False, 'Username already taken.')
                )
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
            return render(
                request,
                'accounts/signup.html',
                create_response(False, 'Passwords do not match.')
            )
    else:
        return render(request, 'accounts/signup.html')

def signin(request):
    """Controls the sign in logic for a typical user"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username != '' and password != '':
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if 'next' in request.POST:
                    response = redirect(request.POST['next'])
                else:
                    response = render(
                        request,
                        'accounts/signin.html',
                        create_response(True, 'Welcome back!')
                    )
            else:
                response = render(
                    request,
                    'accounts/signin.html',
                    create_response(False, 'You do not have an account.')
                )
        else:
            response = render(
                request,
                'accounts/signin.html',
                create_response(False, 'Information is invalid or missing.')
            )
        return response
    else:
        return render(request, 'accounts/signin.html', {'ok': True})

def signout(request):
    """Controls the sign out logic for a typical user"""
    logout(request)
    return render(
        request,
        'accounts/signin.html',
        create_response(True, 'Signed out')
    )

def create_response(status_ok, message) -> Dict:
    """Generate a typical python dictionary response"""
    return {'ok': status_ok, 'message': message}
