from django.forms import ModelForm, ClearableFileInput, TextInput, EmailInput, NumberInput, DateInput, Select, FileInput, Textarea
from .models import Application, Document
from django.core.exceptions import ValidationError

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ('title', 
                  'email',
                  'phone_number',
                  'first_name',
                  'middle_name',
                  'last_name',
                  'date_of_birth',
                  'gender',
                  'employer',
                  'job_title',
                  'photo',
                  'proposal',
                  )
        widgets = {
            'title': Select(attrs={'class': 'input is-small '}),
            'first_name': TextInput(attrs={'placeholder': 'First Name'}),
            'middle_name': TextInput(attrs={'placeholder': 'Middle Name (optional)'}),
            'last_name': TextInput(attrs={'placeholder': 'Last Name'}),
            'email': EmailInput(attrs={'placeholder': 'Email', 'pattern':'^[^@\s]+@[^\s@]+\.[^.\s]{2,}$'}), 
            'phone_number': NumberInput(attrs={'placeholder': 'Phone Number'}),
            'date_of_birth': DateInput(attrs={'type':'date','placeholder':'YYYY-MM-DD'}),
            'gender': Select(attrs={'class': 'input is-small ','style':'width:200px'}),
            'employer': TextInput(attrs={'class': 'input is-small ','placeholder':'Enter name here'}),
            'job_title': TextInput(attrs={'class': 'input is-small ','placeholder':'Enter title here'}),
            'photo': FileInput(attrs={'class':'file-input is-small'}),
            'proposal': Textarea(attrs={'class':'textarea input','placeholder':'Write proposal Here (1000 words)','rows':2,}),
        }
        
    
    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['title'].empty_label = None
        self.fields['title'].choices = [(None, 'title')] + list(self.fields['title'].choices)[1:]
        self.fields['gender'].empty_label = None
        self.fields['gender'].choices = [(None, '')] + list(self.fields['gender'].choices)[1:]
        for name, field in self.fields.items():
            if name == 'photo' or name == 'proposal':
                continue
            field.widget.attrs.update({'class': 'input is-small',})
   
        
        
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