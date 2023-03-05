from django.shortcuts import render,redirect

def LoginUser(request):
    if request.method == 'POST':
        return redirect('dashboard')
    context = {}
    return render(request, 'users/login.html', context)

def Dashboard(request):
    context = {}
    return render(request, 'users/dashboard.html', context)

def Applications(request):
    context = {}
    return render(request, 'users/applications.html', context)

def ApplicationDetail(request):
    context = {}
    return render(request, 'users/application_detail.html', context)