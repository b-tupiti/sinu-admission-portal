from django.forms import ModelForm, ClearableFileInput
from .models import Application, Document
from django.core.exceptions import ValidationError

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
        fields = ['file']
        widgets = {
            'file': ClearableFileInput(attrs={'accept': '.pdf,.doc,.docx'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'file-input',})

        
    def clean_file(self):
        file = self.cleaned_data['file']
        extension = file.name.split('.')[-1].lower()
        if extension not in ['pdf', 'doc', 'docx']:
            raise ValidationError('Invalid file type. Only PDF and Word documents are allowed.')
        return file