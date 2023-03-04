from django.shortcuts import render
from .forms import ApplicationForm, DocumentForm
from django.forms import formset_factory

def submission_form(request):
    """
    displays a form for the user to submit an application
    """
    is_submitted = False
    
    DocumentFormSet = formset_factory(DocumentForm, extra=1)
    document_formset = DocumentFormSet(prefix='document')
    application_form = ApplicationForm()
    
    if request.method == 'POST':
        is_submitted = True
    
    context = {
        'application_form':application_form, 
        'document_formset': document_formset,
        'is_submitted': is_submitted,
    }
    
    return render(request, 'mbasubmission/right-section/template.html',context)
