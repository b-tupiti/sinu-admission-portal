from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages

def LoginUser(request):
    
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request,'this email does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'dashboard')

        else:
            messages.error(request,'your email or password is invalid')
    
    return render(request, 'users/login.html')






def Dashboard(request):
    context = {}
    return render(request, 'users/dashboard.html', context)

def Applications(request):
    context = {}
    return render(request, 'users/applications.html', context)

def ApplicationDetail(request):
    context = {}
    return render(request, 'users/application_detail.html', context)