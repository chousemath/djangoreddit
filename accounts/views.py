from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password_confirmation']:
            User.objects.create_user(
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password']
            )
            return render(request, 'accounts/signup.html', {
                'ok': True,
                'message': 'Welcome to the website!'
            })
        else:
            return render(request, 'accounts/signup.html', {
                'ok': False,
                'message': 'Password and password confirmation do not match.'
            })
    else:
        return render(request, 'accounts/signup.html')
