from django.shortcuts import render,redirect
from .models.user import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from admission.models.application import Application
from admission.models.document import Document
from .utils import filter_applications, get_group
from django.urls import reverse      
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

def login_user(request):
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
            if user.is_staff:
                return redirect('admin:index')
            else:
                return redirect('dashboard')
        else:
            messages.error(request,'your email or password is invalid')
    
    return render(request, 'users/authentication/login.html')


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, 'you signed out!')
    return redirect('login')



@login_required
def dashboard(request):
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
    }
    return render(request, 'users/dashboard/staff_dashboard.html',context)





@login_required(login_url="login")
def applications(request, filter=None):
    
    page = 'applications'
    applications, group = filter_applications(request, filter)
    
    context = {
        'page': page,
        'pending_applications': applications,
        'group': group,
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
def application_detail(request, pk):
    
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
    }
    return render(request, 'users/application/application_template.html', context)

 
@login_required(login_url="login")
def save_application(request, pk):
    application = Application.objects.get(id=pk)
    if request.method == "POST":
       student_id = request.POST.get('student_id')
       application.student_id = student_id
       application.save()
    
    return redirect(reverse('application-detail', args=[pk]))