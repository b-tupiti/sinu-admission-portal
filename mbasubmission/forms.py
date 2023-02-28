from django.forms import ModelForm
from .models import Application, Document

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ('email', 
                  'phone_number',
                  'first_name',
                  'middle_name',
                  'last_name',
                  'photo',
                  'proposal',
                  )
        
class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ('name', 'file')