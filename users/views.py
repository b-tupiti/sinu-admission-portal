from django.shortcuts import render,redirect
from .models.user import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from admission.utils import get_totals
from admission.models import Application, Document, ApplicationState
from .utils import filter_applications, get_group
from django.db.models import Q
from django.urls import reverse      

### 

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group

def group_required(group_name):
    """Check if a user is a member of the specified group"""
    
    def check_group(user):
        try:
            group = Group.objects.get(name=group_name)
        except Group.DoesNotExist:
            return False
        return group in user.groups.all()
    
    return user_passes_test(check_group)

###

def LoginUser(request):
    """Logs in a user"""
    
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
            return redirect('dashboard')
        else:
            messages.error(request,'your email or password is invalid')
    
    return render(request, 'users/authentication/login.html')


def LogoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, 'you signed out!')
    return redirect('login')



@login_required
def Dashboard(request):
    if request.user.is_staff:
        return staff_dashboard(request)
    else:
        return student_dashboard(request)


def student_dashboard(request):
    applications = Application.objects.filter(applicant=request.user)
    context = {'applications':applications}
    return render(request, 'users/dashboard/student_dashboard.html',context)




def staff_dashboard(request):
    page = 'dashboard'
    group = get_group(request)

    context = {
        'page': page,
        'group': group,
        'totals': get_totals(),
    }
    return render(request, 'users/dashboard/staff_dashboard.html',context)





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
    return render(request, 'users/applications_list.html', context)



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
    return render(request, 'users/application/application_template.html', context)

 
@login_required(login_url="login")
def SaveId(request, pk):
    application = Application.objects.get(id=pk)
    if request.method == "POST":
       student_id = request.POST.get('student_id')
       application.student_id = student_id
       application.save()
    
    return redirect(reverse('application-detail', args=[pk]))