from django.shortcuts import render
from .forms import ApplicationForm, DocumentForm
from django.forms import formset_factory
from .models import Application, Document, ApplicationToken


def submission_form(request):
    """
    displays a form for the user to submit an application
    """
    is_submitted = False
    
    DocumentFormSet = formset_factory(DocumentForm, extra=1)
    document_formset = DocumentFormSet(prefix='document')
    application_form = ApplicationForm()
    
    if request.method == 'POST':
        
        # get photos and all documents
        photo = request.FILES['photo']
        doc_keys = [key for key in request.FILES if key != 'photo']
        documents = [request.FILES[key] for key in doc_keys]
        
        application_form = ApplicationForm(request.POST, {'photo': photo})
        
        if application_form.is_valid():
            application = application_form.save()
            for document in documents:
                Document.objects.create(file=document,application=application)

        is_submitted = True
    
    context = {
        'application_form':application_form, 
        'document_formset': document_formset,
        'is_submitted': is_submitted,
    }
    
    return render(request, 'mbasubmission/right-section/template.html',context)


def upload_receipt(request):
    
    token = request.GET.get('token')
    context = {}
    
    try:
        token = ApplicationToken.objects.get(id=token)
        application = Application.objects.get(id=token.application.id)
        context['application'] = application
    except ApplicationToken.DoesNotExist:
        pass
    
    return render(request, 'receipt/upload_receipt.html', context)
    