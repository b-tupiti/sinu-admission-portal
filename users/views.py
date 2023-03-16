from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from mbasubmission.utils import get_totals
from mbasubmission.models import Application, Document
from .utils import filter_applications, get_group
from django.db.models import Q
from django.urls import reverse      

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


def LogoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, 'you signed out!')
    return redirect('login')




@login_required(login_url="login")
def Dashboard(request):
    page = 'dashboard'
    group = get_group(request)

    context = {
        'page': page,
        'group': group,
        'totals': get_totals(),
    }
    return render(request, 'users/dashboard.html',context)








@login_required(login_url="login")
def Applications(request, filter=None):
    
    page = 'applications'
    applications, group = filter_applications(request, filter)
    
    context = {
        'page': page,
        'pending_applications': applications,
        'group': group,
        'totals': get_totals(),
    }
    return render(request, 'users/applications.html', context)



def process_application(request, pk):
    
    application = Application.objects.get(id=pk)
    print(request.POST['action'])
    if request.POST['action'] == 'proceed_to_assessment':
        application.application_state = Application.ApplicationState.UNDER_ASSESSMENT
        application.save()
    elif request.POST['action'] == 'confirm_enrolment':
        application.application_state = Application.ApplicationState.ENROLLMENT_COMPLETE
        application.save()
    elif request.POST['action'] == 'clear_for_enrolment':
        application.application_state = Application.ApplicationState.CLEARED_FOR_ENROLLMENT
        application.save()
    elif request.POST['action'] == 'accept_application':
        application.application_state = Application.ApplicationState.OFFER_LETTER_ISSUED
        application.save()




@login_required(login_url="login")
def ApplicationDetail(request, pk):
    
    if request.method == 'POST':
        process_application(request, pk)
    
    page = 'application-detail'
    group = get_group(request)

    application = Application.objects.get(id=pk)
    documents = Document.objects.filter(application=application)
    context = {
        'page': page,
        'group': group,
        'application': application,
        'documents': documents,
        'totals': get_totals(),
    }
    return render(request, 'users/application_detail.html', context)

 
@login_required(login_url="login")
def SaveId(request, pk):
    application = Application.objects.get(id=pk)
    if request.method == "POST":
       student_id = request.POST.get('student_id')
       application.student_id = student_id
       application.save()
    
    return redirect(reverse('application-detail', args=[pk]))