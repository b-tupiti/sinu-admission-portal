from django.shortcuts import render

def submission_form(request):
    
    context = {}
    return render(request, 'mbasubmission/submission_form.html',context)
